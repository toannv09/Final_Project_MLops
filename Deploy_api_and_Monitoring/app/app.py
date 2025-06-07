from fastapi import FastAPI, HTTPException, Request, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Summary, Counter
from PIL import Image
from torchvision import models, transforms
import torch
import torch.nn as nn
import json
import logging
import time
import sys
import os
from logging.handlers import SysLogHandler

# ============ CONFIG ============ #
MODEL_PATH = "model.pth"
CLASS_NAMES_FILE = "class_names.json"
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app_log.log")
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# ================================ #

# ============ Logging Setup ============ #
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.handlers.clear()

file_handler = logging.FileHandler(LOG_FILE, mode='a')
stdout_handler = logging.StreamHandler(sys.stdout)
stderr_handler = logging.StreamHandler(sys.stderr)
file_handler.setLevel(logging.INFO)
stdout_handler.setLevel(logging.INFO)
stderr_handler.setLevel(logging.ERROR)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

try:
    syslog_handler = SysLogHandler(address="/dev/log")
    syslog_handler.setLevel(logging.INFO)
    logger.addHandler(syslog_handler)
except Exception as e:
    logger.warning(f"Không thể kết nối syslog: {e}")

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
for handler in logger.handlers:
    handler.setFormatter(formatter)

logger.info("=== APPLICATION STARTING ===")
logger.info(f"Log file: {LOG_FILE}")
# ========================================= #

# Load class names
with open(CLASS_NAMES_FILE, "r") as f:
    CLASS_NAMES = json.load(f)
logger.info("Class names loaded")

# Load model
model = models.efficientnet_b0(pretrained=False)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, 30)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.to(DEVICE)
model.eval()
logger.info("Model loaded successfully")

# Preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std =[0.229, 0.224, 0.225])
])

# Prometheus metrics
INFERENCE_TIME = Summary("inference_time_seconds", "Time taken for inference")
CONFIDENCE_SCORE_SUM = Counter("confidence_score_sum", "Sum of confidence scores")
CONFIDENCE_SCORE_COUNT = Counter("confidence_score_count", "Count of confidence scores")

# FastAPI app
app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Kiểm tra định dạng
        filename = file.filename.lower()
        if not (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png")):
            msg = "Chỉ hỗ trợ ảnh .jpg, .jpeg, .png"
            logger.warning(msg)
            raise HTTPException(status_code=400, detail=msg)

        if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
            msg = f"MIME không hợp lệ: {file.content_type}. Chỉ chấp nhận JPEG/PNG"
            logger.warning(msg)
            raise HTTPException(status_code=400, detail=msg)

        # Đọc ảnh
        image = Image.open(file.file).convert("RGB")
        input_tensor = transform(image).unsqueeze(0).to(DEVICE)

        # Dự đoán
        start = time.time()
        with INFERENCE_TIME.time():
            with torch.no_grad():
                output = model(input_tensor)
        end = time.time()

        prob = torch.softmax(output, dim=1)
        confidence, pred_class = torch.max(prob, 1)
        confidence = confidence.item()
        label = CLASS_NAMES[pred_class.item()]

        CONFIDENCE_SCORE_SUM.inc(confidence)
        CONFIDENCE_SCORE_COUNT.inc()

        logger.info(f"Prediction: {label}, Confidence: {confidence:.2f}, Time: {end - start:.3f}s")

        return {
            "class": label,
            "confidence": round(confidence, 4),
            "inference_time": round(end - start, 4)
        }

    except Exception as e:
        logger.exception("Prediction error")
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý ảnh: {str(e)}")

@app.get("/health")
def health_check():
    logger.info("Health check OK")
    return {"status": "ok"}

@app.get("/error500")
def error_500():
    logger.error("Error 500 triggered")
    raise HTTPException(status_code=500, detail="Internal Server Error for testing")

# Global exception handler
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException: {exc.detail}")
    return await http_exception_handler(request, exc)

@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=5000)
