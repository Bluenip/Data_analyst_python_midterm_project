# Slide thuyết trình midterm

[**presentation_midterm.pdf**](presentation_midterm.pdf) gồm **14 slide**, đáp ứng yêu cầu 10–15 slide trong `../Mid-Term.pdf`. Nội dung tiếng Anh thống nhất với báo cáo; tên thành viên và giảng viên giữ dấu tiếng Việt.

Slide tóm tắt bài toán, ba bảng dữ liệu, làm sạch, EDA, thiết kế thí nghiệm, năm nhóm đặc trưng, bốn thuật toán, kết quả validation/test, baseline, confusion matrix, ROC, nhóm ID mới và các giới hạn. Số liệu lấy từ output đã lưu trong `../mid_term_code.ipynb` và `../report/bao_cao_midterm.tex`; biểu đồ dùng lại các tệp trong `../report/figures/`.

## Tạo lại PDF

Từ thư mục gốc repository, dùng Python 3.11 trở lên:

```bash
python -m pip install -r slides/requirements.txt
python slides/build_slides.py
```

Nguồn có thể chỉnh sửa là [build_slides.py](build_slides.py). Script tự xác định đường dẫn theo vị trí của nó, sử dụng logo và font đã có trong `report/`, và tạo PDF tỷ lệ 16:9 với chữ/vector cùng ảnh biểu đồ. Không cần chạy lại mô hình để dựng slide. Script có kiểm tra số slide và chiều rộng/chiều cao các khối chữ.

Sau khi thay đổi notebook, đối chiếu lại các số liệu trong nguồn slide và báo cáo, cập nhật các hình tương ứng rồi tạo lại PDF. Các số trên slide được làm tròn như báo cáo; số liệu là snapshot của lần thực thi đã được rà soát, không tự cập nhật từ một lần chạy notebook mới.

## Trình chiếu

Mở PDF ở chế độ toàn màn hình. Thứ tự slide: bài toán → dữ liệu → làm sạch → EDA → thiết kế → đặc trưng → mô hình → validation → test → lỗi/ROC → nhóm ID → kết luận. Phần giới hạn nêu rõ test đã được xem trong quá trình phát triển và chưa đánh giá chất lượng xếp hạng gợi ý.
