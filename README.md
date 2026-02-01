<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS317.P21 - PHÁT TRIỂN VÀ VẬN HÀNH HỆ THỐNG MÁY HỌC</b></h1>

## ĐỒ ÁN: VIETNAMESE FOOD CLASSIFICATION 

## GIỚI THIỆU MÔN HỌC
<a name="gioithieumonhoc"></a>
* *Tên môn học*: Phát triển và vận hành hệ thống máy học
* *Mã môn học*: CS317.P21
* *Ngày bắt đầu*: 17/02/2025
* *Năm học*: 2024-2025

## GIẢNG VIÊN HƯỚNG DẪN
<a name="giangvien"></a>
* *Đỗ Văn Tiến* - tiendv@uit.edu.vn
* *Lê Trần Trọng Khiêm* - khiemltt@uit.edu.vn

## THÀNH VIÊN NHÓM
<a name="thanhvien"></a>
* Nguyễn Vẹn Toàn - 22521492
* Đào Văn Tuân - 22521599
* Vũ Anh Tuấn - 22521614

## PIPIELINE
![image](https://github.com/user-attachments/assets/12a25bdf-02d7-44fc-886c-84bb236269e0)

## LINK DEMO
https://huggingface.co/spaces/Lippovn04/Vietnamese-Food-Classification

## HƯỚNG DẪN TRACKING
Tải file vnfood-tracking.ipynb. Sau đó upload lên kaggle để sử dụng. Dataset nhóm sử dụng là 30VNFoods cũng có trên Kaggle.<br>
Công cụ tracking được nhóm lựa chọn sử dụng là Weight & Biases (Wandb). Dưới đây là các bước thực hiện cho quá trình tracking:<br><br>
a.	Đăng nhập<br>
Để có thể sử dụng Wandb cho mục đích track lại dữ liệu trong quá trình huấn luyện, ta cần tích hợp với session làm việc bằng API key được cung cấp từ tài khoản Wandb.<br>
 ![image](https://github.com/user-attachments/assets/86d38870-3776-4510-a22b-7379df1f629f)<br>

Vì nhóm làm việc trên nền tảng Kaggle, website có sẵn chức năng Secrets gán API key với một từ khóa (cụ thể trong hình là WANDB) để tránh việc phải paste cả key vào code, làm lộ mất key cho người khác thấy được.<br><br>
b.	Triển khai<br>
Sau khi đã đăng nhập vào session huấn luyện, ta cần thực hiện việc triển khai tracking. Việc triển khai yêu cầu phải nhập vào các thông tin về lượt run như là tên dự án, thông số mô hình…<br>
 ![image](https://github.com/user-attachments/assets/18518fec-810d-4801-835f-87037ba55eaa)<br>

c.	Log dữ liệu và kết thúc<br>
Tiếp theo, ta cần phải thêm các đoạn code để lưu lại những dữ liệu mong muốn trong lượt run này.<br>
 ![image](https://github.com/user-attachments/assets/01059e1a-0dae-4245-89a7-0dcbedac2bac)
 ![image](https://github.com/user-attachments/assets/12839361-fedb-4454-bee8-7445ff537d02)
 ![image](https://github.com/user-attachments/assets/c3353598-ec36-41e9-9efc-7a7cdefc6abe)
 ![image](https://github.com/user-attachments/assets/49ecaad2-071c-4b25-84ef-c3c211f375dc)
 ![image](https://github.com/user-attachments/assets/7c80f034-b35a-4b10-9e7a-b074031159fc)
 ![image](https://github.com/user-attachments/assets/200c66b1-7a0c-44f5-ab81-ed1bf50d8010)<br>
 
Ngoài ra, Wandb còn có cả chức năng save lại checkpoint của model tốt nhất.<br>
 ![image](https://github.com/user-attachments/assets/11bfeed9-d42a-46ad-a16c-59a72c58eba1)<br>

Sau khi đã log lại toàn bộ những gì cần thiết, ta cần phải có lệnh dừng tracking sau khi đã xong lượt run (quan trọng).<br>
 ![image](https://github.com/user-attachments/assets/bb29f216-35a3-4335-bcca-76301c982f5a)<br>

Nếu không có lệnh này, Wandb sẽ vẫn tiếp tục thực hiện việc tracking cho dù quá trình huấn luyện đã hoàn tất, dẫn đến việc tiêu hao tài nguyên và nguy cơ gặp lỗi lưu dữ liệu nếu tìm cách dừng đột ngột.<br><br>
d.	Giao diện Wandb<br>
 ![image](https://github.com/user-attachments/assets/3d63ddba-5b56-4988-b5ea-687cb67f33a9)<br>
Giao diện overview của lượt run, đây là nơi để xem thông tin khái quát như tên dự án, tham số, dataset, thời gian huấn luyện….<br>

 ![image](https://github.com/user-attachments/assets/0c8ec69c-5a6d-4ade-a23b-0209c96de876)<br>
Giao diện Workspace, đây là nơi để kiểm tra lại các dữ liệu được log<br>
 
 ![image](https://github.com/user-attachments/assets/1cfca0c0-6d33-464a-87df-f9911629fcda)<br>
Giao diện log, chứa log của đoạn code trong quá trình chạy<br>

 ![image](https://github.com/user-attachments/assets/0a8a55ee-048e-4edf-aa9a-774776b34db8)<br>
Giao diện Files, là nơi chứa gốc rễ thư mục, có thể tìm thấy dữ liệu đã được log ở đây dưới dạng file<br>

---
# HƯỚNG DẪN MONITORING, ALERTING VÀ LOGGING
## 📁 Chuẩn bị thư mục
1.	Tải folder Deploy_api_and_Monitoring cùng toàn bộ nội dung bên trong.
2.	Tải file grafana_dashboard_model.json và đặt vào cùng thư mục Deploy_api_and_Monitoring.

---

## 🖥️ Cài đặt & chạy trên máy local

### 🔹 Trường hợp 1: Dùng image có sẵn từ DockerHub *(Nhanh gọn)*

Không cần build lại image, chỉ cần chạy:

```bash
docker compose up
```

📝 *Mặc định `docker-compose.yml` đã sử dụng image có sẵn từ DockerHub:*

```yaml
image: <your-dockerhub-username>/<your-image-name>
```

---

### 🔹 Trường hợp 2: Tự build image từ mã nguồn

1. Mở file `docker-compose.yml`
2. Tìm dòng:

```yaml
image: <your-dockerhub-username>/<your-image-name>
```

3. **Xóa dòng này** hoặc thay bằng tên image tùy chọn, ví dụ:

```yaml
image: my-fastapi-app:latest
```

4. Chạy lệnh sau để build và khởi động:

```bash
docker compose up --build
```

⚠️ *Nếu không chỉnh sửa `image:` thì Docker sẽ tiếp tục dùng image từ DockerHub.*

---

### 🔍 Kiểm tra API

Mở trình duyệt truy cập:  
👉 [http://localhost:5050/docs](http://localhost:5050/docs)

🛑 Để dừng ứng dụng:  
Nhấn `Ctrl + C` trong terminal

---

## 📈 Truy cập Grafana để xem Monitoring & Logging

1. Mở trình duyệt:
   - Local: [http://localhost:3000](http://localhost:3000)
   - Server: [http://<ip_server>:3000](http://<ip_server>:3000)

2. Đăng nhập:
   - **Username:** `admin`
   - **Password:** `admin` (sẽ yêu cầu đổi mật khẩu sau lần đăng nhập đầu tiên)

---

## ⚙️ Cấu hình Grafana

1. **Thêm Data Source**
   - Vào `Connections` → `Data Sources` → `Add data source`
   - **Chọn Prometheus:**
     - Name: `prometheus`
     - URL: `http://prometheus:9090`
     - Save & Test
   - **Chọn Loki:**
     - Name: `loki`
     - URL: `http://loki:3000`
     - Save & Test

---

2. **Thêm Dashboards**

🔹 **Dashboard 1:**

- Vào `Dashboards` → `New` → `Import`
- Nhập ID: `1860` → Load → Load

📊 *Hiển thị: CPU usage, RAM usage, Disk space, disk IO, Network IO (Tx/Rx)*

🔹 **Dashboard 2:**

- Vào `Dashboards` → `New` → `Import`
- Upload file: `grafana_dashboard_model.json` → Load

📊 *Hiển thị: Request per second, Error rate, Latency, Inference speed, Confidence score*

---

## 📜 Xem log với Loki

1. Vào một dashboard → `Add visualization`
2. Chọn **Data source:** `loki`
3. Phần `Queries` nhập một trong các dòng sau để lọc log:

```
# 1. App logs
{job="app_logfile"}

# 2. Docker stdout/stderr
{job="docker_stdout"}

# 3. Chỉ stdout
{job="docker_stdout", stream="stdout"}

# 4. Chỉ stderr
{job="docker_stdout", stream="stderr"}

# 5. Syslog
{job="syslog"}
```

Có thể tùy chỉnh và lưu lại visualization theo nhu cầu.
