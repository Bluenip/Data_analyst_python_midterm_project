# Phân loại đánh giá sách — Book Recommendation Dataset

Dự án phân tích dữ liệu sách, người dùng và các lượt đánh giá để dự đoán một lượt đánh giá thuộc nhóm **điểm cao (8–10)** hay **điểm 1–7**. Nhãn `liked = 1` được quy ước cho điểm từ 8 trở lên; nhãn 0 không đồng nghĩa với việc người dùng không thích sách. Điểm 0 là phản hồi ngầm, được giữ trong thống kê hoạt động nhưng không dùng làm nhãn hoặc tính điểm trung bình.

- [Notebook phân tích và kết quả thực thi](mid_term_code.ipynb)
- [Báo cáo phân tích PDF](report/bao_cao_midterm.pdf)
- [Mã nguồn LaTeX](report/bao_cao_midterm.tex) và [hướng dẫn biên dịch](report/README.md)
- [Slide thuyết trình PDF — 15 trang](slides/presentation_midterm.pdf) và [hướng dẫn tạo lại](slides/README.md)

**Thành viên:** Lương Văn Thái Tuấn — 11258665; Nguyễn Thị Khánh Hòa — 11253156.

**Giảng viên hỗ trợ:** Tiến sĩ Trần Đức Minh.

## Nội dung phân tích

1. Kiểm tra cấu trúc, mã hóa, khóa và quan hệ giữa ba bảng dữ liệu.
2. Ghép dữ liệu, chuẩn hóa ISBN, xử lý dữ liệu trùng, thiếu và bất thường.
3. Phân tích phân bố điểm, độ tuổi, mức hoạt động của người dùng và đặc điểm đánh giá sách.
4. Xây dựng đặc trưng và so sánh bốn thuật toán phân loại qua năm nhóm đầu vào.
5. Chọn phương án trên validation, đánh giá trên test, so sánh baseline và phân tích giới hạn.

Notebook chứa code, chú thích, biểu đồ và output đã lưu. Báo cáo trình bày phương pháp, diễn giải kết quả, mười hình và bảng so sánh đầy đủ 20 phương án.

Bộ slide tóm tắt bài toán, dữ liệu, phương pháp, kết quả và giới hạn trong 15 trang, đáp ứng yêu cầu 10–15 slide của đề bài. PDF dùng để trình chiếu; mã nguồn Python được đính kèm để chỉnh sửa và tạo lại.

## Dữ liệu

Nguồn: [Book Recommendation Dataset — Möbius, Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset). [Mô tả của người cung cấp](https://www.kaggle.com/discussions/general/202108) phân biệt điểm 1–10 là đánh giá tường minh và điểm 0 là phản hồi ngầm.

| Tệp | Số dòng gốc | Nội dung |
|---|---:|---|
| `Books.csv` | 271.360 | ISBN, tên sách, tác giả, năm xuất bản, nhà xuất bản và URL ảnh |
| `Users.csv` | 278.858 | Mã người dùng, vị trí và tuổi |
| `Ratings.csv` | 1.149.780 | Mã người dùng, ISBN và điểm đánh giá |

Sau làm sạch và chọn điểm 1–10, tập phân loại có **433.671 lượt đánh giá**: 249.887 lượt thuộc nhãn 1 và 183.784 lượt thuộc nhãn 0. ISBN được giữ ở dạng chuỗi để bảo toàn số 0 đầu và ký tự X; left join giữ các lượt chưa có metadata sách.

## Cấu trúc thư mục

```text
Data_analyst_python_midterm_project/
├── mid_term_code.ipynb
├── requirements.txt
├── README.md
├── Mid-Term.pdf                 # Đề bài
├── DATA_SET/
│   ├── Books.csv
│   ├── Users.csv
│   └── Ratings.csv
├── report/
│   ├── bao_cao_midterm.pdf      # Báo cáo phân tích
│   ├── bao_cao_midterm.tex
│   ├── README.md
│   ├── neu_logo.png
│   ├── fda_logo.png
│   ├── figures/
│   └── fonts/
└── slides/
    ├── presentation_midterm.pdf # 15 slide thuyết trình
    ├── build_slides.py          # Mã nguồn tạo slide
    ├── requirements.txt
    └── README.md
```

## Chạy trên Jupyter

Dùng Python 3.11 trở lên. Mở terminal tại thư mục dự án:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user --name book-midterm --display-name "Python (Book Midterm)"
python -m jupyterlab
```

Trên Windows, kích hoạt môi trường bằng `.venv\Scripts\activate`.

Mở `mid_term_code.ipynb`, chọn kernel **Python (Book Midterm)** và chạy **Restart Kernel → Run All**. Notebook có 42 cell code và huấn luyện 20 phương án; thời gian chạy tùy cấu hình máy. Thư mục làm việc phải chứa `DATA_SET`; nếu dữ liệu ở nơi khác, sửa `DATA_DIR` trong ô thiết lập. Phiên bản thư viện thực tế được in ở đầu notebook.

## Chạy trên Google Colab

Mở notebook từ GitHub trong Colab (**File → Open notebook → GitHub**, dán link repository) rồi chọn **Runtime → Run all**. Ô thiết lập đầu notebook tự nhận biết Colab: nếu chưa có `DATA_SET`, notebook clone repository vào `/content/Data_analyst_python_midterm_project` (khoảng 100 MB) và đọc dữ liệu từ đó. Lệnh clone chỉ chạy một lần cho mỗi runtime.

Các thư viện cần dùng đã có sẵn trên Colab; nếu thiếu, cài bằng `pip install -r requirements.txt` rồi khởi động lại runtime. Có thể đặt `DATA_DIR` thành đường dẫn tuyệt đối tới dữ liệu trên Google Drive.

## Thiết kế thí nghiệm

- **Chia dữ liệu:** train 70%, validation 15%, test 15%; phân tầng theo nhãn, seed 56.
- **Thuật toán:** Logistic Regression, Decision Tree, Linear SVM và MLP.
- **Nhóm đặc trưng:** Initial → Metadata → Country → Count → Target Encoding. Mỗi bước thêm một nhóm đầu vào, giữ nguyên cách chia và cấu hình của từng thuật toán.
- **Tiền xử lý:** median, chuẩn hóa và One-Hot chỉ học từ train. Biến đếm tra thống kê train; tỷ lệ nhãn dùng OOF 5 fold với smoothing α = 20 cho train, thống kê toàn train cho validation/test.
- **Lựa chọn:** Macro F1 cao nhất trên validation trong cả 20 phương án; khi bằng nhau xét ROC-AUC rồi Accuracy.
- **Đánh giá:** Accuracy, Precision, Recall, F1, Macro F1, ROC-AUC, confusion matrix và kết quả theo nhóm người dùng/sách đã gặp hoặc chưa gặp trong train.

## Kết quả

Phương án được chọn là **Logistic Regression với Target Encoding**.

| Chỉ số trên test | Kết quả |
|---|---:|
| Accuracy | 65,65% |
| Macro F1 | 0,6553 |
| ROC-AUC | 0,7306 |

So với baseline luôn dự đoán nhãn phổ biến, Accuracy tăng **8,03 điểm phần trăm** và Macro F1 tăng **0,2897**. F1 riêng của nhãn 1 giảm, cho thấy mô hình cải thiện khả năng nhận diện cả hai nhóm nhưng không tốt hơn baseline ở mọi chỉ số. Xem notebook và báo cáo để đọc đầy đủ các kết quả so sánh.

## Phạm vi và giới hạn

Kết quả áp dụng cho các lượt có điểm 1–10 trong dữ liệu quan sát. Chia ngẫu nhiên theo lượt cho phép cùng người dùng hoặc sách xuất hiện ở nhiều tập; chưa đánh giá thuần khả năng dự đoán cho người dùng/sách mới hoặc theo thời gian. Tuổi và metadata còn thiếu; quốc gia được trích từ thông tin tự khai.

EDA dùng toàn mẫu và test đã được xem trong quá trình phát triển, nên cần dữ liệu giữ lại mới để xác nhận độc lập. Các chỉ số phân loại hiện tại chưa đo chất lượng xếp hạng của một hệ thống gợi ý sách. Kết quả cũng có thể chênh lệch nhẹ giữa các phiên bản thư viện hoặc thư viện tính toán số.
