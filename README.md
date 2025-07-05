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

## HƯỚNG DẪN TRACKING
Tải file vnfood-tracking.ipynb. Sau đó upload lên kaggle để sử dụng. Dataset nhóm sử dụng là 30VNFoods cũng có trên Kaggle.
Công cụ tracking được nhóm lựa chọn sử dụng là Weight & Biases (Wandb). Dưới đây là các bước thực hiện cho quá trình tracking:
a.	Đăng nhập
Để có thể sử dụng Wandb cho mục đích track lại dữ liệu trong quá trình huấn luyện, ta cần tích hợp với session làm việc bằng API key được cung cấp từ tài khoản Wandb.
 ![image](https://github.com/user-attachments/assets/86d38870-3776-4510-a22b-7379df1f629f)

Vì nhóm làm việc trên nền tảng Kaggle, website có sẵn chức năng Secrets gán API key với một từ khóa (cụ thể trong hình là WANDB) để tránh việc phải paste cả key vào code, làm lộ mất key cho người khác thấy được.
b.	Triển khai
Sau khi đã đăng nhập vào session huấn luyện, ta cần thực hiện việc triển khai tracking. Việc triển khai yêu cầu phải nhập vào các thông tin về lượt run như là tên dự án, thông số mô hình…
 ![image](https://github.com/user-attachments/assets/18518fec-810d-4801-835f-87037ba55eaa)

c.	Log dữ liệu và kết thúc
Tiếp theo, ta cần phải thêm các đoạn code để lưu lại những dữ liệu mong muốn trong lượt run này.
 ![image](https://github.com/user-attachments/assets/01059e1a-0dae-4245-89a7-0dcbedac2bac)
 ![image](https://github.com/user-attachments/assets/12839361-fedb-4454-bee8-7445ff537d02)
 ![image](https://github.com/user-attachments/assets/c3353598-ec36-41e9-9efc-7a7cdefc6abe)
 ![image](https://github.com/user-attachments/assets/49ecaad2-071c-4b25-84ef-c3c211f375dc)
 ![image](https://github.com/user-attachments/assets/7c80f034-b35a-4b10-9e7a-b074031159fc)
 ![image](https://github.com/user-attachments/assets/200c66b1-7a0c-44f5-ab81-ed1bf50d8010)
 
Ngoài ra, Wandb còn có cả chức năng save lại checkpoint của model tốt nhất.
 ![image](https://github.com/user-attachments/assets/11bfeed9-d42a-46ad-a16c-59a72c58eba1)

Sau khi đã log lại toàn bộ những gì cần thiết, ta cần phải có lệnh dừng tracking sau khi đã xong lượt run (quan trọng).
 ![image](https://github.com/user-attachments/assets/bb29f216-35a3-4335-bcca-76301c982f5a)

Nếu không có lệnh này, Wandb sẽ vẫn tiếp tục thực hiện việc tracking cho dù quá trình huấn luyện đã hoàn tất, dẫn đến việc tiêu hao tài nguyên và nguy cơ gặp lỗi lưu dữ liệu nếu tìm cách dừng đột ngột.
d.	Giao diện Wandb
 ![image](https://github.com/user-attachments/assets/3d63ddba-5b56-4988-b5ea-687cb67f33a9)
Giao diện overview của lượt run, đây là nơi để xem thông tin khái quát như tên dự án, tham số, dataset, thời gian huấn luyện….

 ![image](https://github.com/user-attachments/assets/0c8ec69c-5a6d-4ade-a23b-0209c96de876)
Giao diện Workspace, đây là nơi để kiểm tra lại các dữ liệu được log
 
 ![image](https://github.com/user-attachments/assets/1cfca0c0-6d33-464a-87df-f9911629fcda)
Giao diện log, chứa log của đoạn code trong quá trình chạy

 ![image](https://github.com/user-attachments/assets/0a8a55ee-048e-4edf-aa9a-774776b34db8)
Giao diện Files, là nơi chứa gốc rễ thư mục, có thể tìm thấy dữ liệu đã được log ở đây dưới dạng file
