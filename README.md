# Midterm — Phân loại đánh giá sách

Đề 6 trong [Mid-Term.pdf](Mid-Term.pdf): dự đoán một lượt đánh giá có điểm **8–10** (`liked = 1`) hay **1–7** (`liked = 0`). Ngưỡng 8 là quy ước của nhóm. Điểm 0 là phản hồi ngầm theo nguồn dữ liệu, không dùng làm target hoặc tính điểm trung bình.

Notebook chính: [mid_term_code.ipynb](mid_term_code.ipynb). Notebook chứa toàn bộ bước đọc, ghép và làm sạch dữ liệu, EDA, huấn luyện, đánh giá và kết luận. Các bảng và nhận xét định lượng được tính từ kết quả thực thi, không chép cứng số liệu mô hình.

Báo cáo phân tích PDF là bài nộp riêng theo đề. Bản repository hiện tại chưa có file báo cáo hoặc mã nguồn LaTeX; `Mid-Term.pdf` là đề bài. Có thể dùng bảng, hình và phần diễn giải trong notebook để viết báo cáo.

## Dữ liệu và nguồn

[Book Recommendation Dataset — Möbius, Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset), kèm [mô tả các loại đánh giá của người cung cấp](https://www.kaggle.com/discussions/general/202108).

Giữ cấu trúc sau khi tải hoặc clone dự án:

```text
Data_analyst_python_midterm_project/
├── mid_term_code.ipynb
├── requirements.txt
├── Mid-Term.pdf
└── DATA_SET/
    ├── Books.csv
    ├── Users.csv
    └── Ratings.csv
```

Ba bảng gốc có 271.360 sách, 278.858 người dùng và 1.149.780 lượt đánh giá. Notebook giữ ISBN ở dạng chuỗi, chuẩn hóa khoảng trắng trong khóa, kiểm tra xung đột và dùng left join để giữ các lượt thiếu metadata sách.

## Chạy trên Jupyter

Đề xuất Python 3.11 trở lên. Mở terminal tại thư mục dự án:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user --name book-midterm --display-name "Python (Book Midterm)"
python -m jupyterlab
```

Trên Windows, kích hoạt bằng `.venv\Scripts\activate` thay cho lệnh `source`.

Mở notebook, chọn kernel **Python (Book Midterm)**, rồi **Restart Kernel → Run All**. Thư mục làm việc phải chứa `DATA_SET`; nếu đặt dữ liệu ở nơi khác, sửa `DATA_DIR` ở ô đầu tiên. Quá trình chạy huấn luyện 20 phương án trên toàn bộ dữ liệu, có thể mất nhiều phút tùy máy. Môi trường và phiên bản thư viện thực tế được in ở đầu notebook; kết quả có thể chênh lệch nhẹ giữa các phiên bản hoặc thư viện BLAS.

## Chạy trên Google Colab

Mở `mid_term_code.ipynb` từ GitHub trong Colab. Notebook mở từ GitHub không tự đưa các CSV vào runtime; thêm một ô thiết lập ở đầu notebook và chạy:

```python
!git clone https://github.com/Bluenip/Data_analyst_python_midterm_project.git
%cd Data_analyst_python_midterm_project
```

Sau đó chạy các ô phân tích còn lại. Nếu Colab đã cung cấp các thư viện phù hợp trong `requirements.txt`, có thể dùng môi trường sẵn có; nếu thiếu, cài gói cần thiết rồi khởi động lại runtime. Có thể thay `DATA_DIR` bằng đường dẫn tuyệt đối tới ba CSV trên Google Drive. Ô clone chỉ cần chạy một lần cho mỗi runtime; nếu thư mục đã tồn tại, chỉ cần lệnh `%cd` với đường dẫn phù hợp.

## Thiết kế và cách đọc kết quả

- Chia theo lượt đánh giá: train 70%, validation 15%, test 15%; phân tầng nhãn, seed chia dữ liệu 56.
- Bốn thuật toán: Logistic Regression, Decision Tree, Linear SVM, MLP. Giữ cấu hình của từng thuật toán cố định qua các nhóm đặc trưng.
- Năm nhóm đầu vào: **Initial → Metadata → Country → Count → Target Encoding**. Mỗi bước chỉ thêm nhóm được nêu; so sánh cùng thuật toán trên cùng validation.
- Median, chuẩn hóa và One-Hot chỉ học từ train. Biến đếm tra train; target encoding dùng OOF 5 fold và smoothing α = 20 cho train, thống kê toàn train cho validation/test.
- Chọn trong cả 20 phương án bằng Macro F1 validation; khi bằng nhau xét ROC-AUC rồi Accuracy. Test chỉ dùng sau khi chốt phương án. Báo cáo đủ Accuracy, Precision, Recall từng nhãn, F1, Macro F1, ROC-AUC, confusion matrix, ROC và baseline.

Kết quả mô tả các lượt có điểm 1–10 trong quần thể quan sát; không trực tiếp đo chất lượng một hệ thống gợi ý xếp hạng. Chia theo lượt cho phép cùng người dùng hoặc sách xuất hiện ở nhiều tập. Test đã được xem ở các phiên bản trước, nên cần dữ liệu giữ lại mới nếu muốn xác nhận độc lập sau quá trình điều chỉnh. Notebook nêu rõ các giới hạn này và báo cáo thêm kết quả theo nhóm ID đã gặp/chưa gặp.

## Các thành phần bài nộp

1. Notebook có code, giải thích và output.
2. Repository GitHub public chứa bản cuối.
3. Báo cáo phân tích PDF riêng (cần bổ sung; chưa có trong repository hiện tại).

Theo xác nhận mới của giảng viên qua người thực hiện dự án, **không cần slide**. `Mid-Term.pdf` là **đề bài**, không phải báo cáo phân tích.
