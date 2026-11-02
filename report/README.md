# Báo cáo midterm — Phân loại đánh giá sách

Đọc bản hoàn chỉnh tại [bao_cao_midterm.pdf](bao_cao_midterm.pdf). File [bao_cao_midterm.tex](bao_cao_midterm.tex) là mã nguồn; các thư mục `figures/`, `fonts/` và `neu_logo.png` là tài nguyên cần để biên dịch. Logo NEU do nhóm cung cấp.

Thành viên: Lương Văn Thái Tuấn — 11258665; Nguyễn Thị Khánh Hòa — 11253156. Giảng viên hỗ trợ: Tiến sĩ Trần Đức Minh.

## Biên dịch trên Overleaf

1. Tạo một project mới, tải toàn bộ **nội dung** thư mục `report/` vào project, giữ cấu trúc thư mục con.
2. Chọn `bao_cao_midterm.tex` làm Main document và **XeLaTeX** làm Compiler.
3. Recompile; nếu mục lục hoặc tham chiếu chưa cập nhật, biên dịch lại.

## Biên dịch trên máy

Cần TeX Live hoặc MiKTeX có XeLaTeX và các gói khai báo ở đầu mã nguồn. Từ thư mục gốc repository:

```bash
cd report
xelatex -interaction=nonstopmode -halt-on-error bao_cao_midterm.tex
xelatex -interaction=nonstopmode -halt-on-error bao_cao_midterm.tex
```

Có thể dùng Tectonic thay cho hai lệnh XeLaTeX:

```bash
tectonic bao_cao_midterm.tex
```

Các font dùng cho nội dung và tên tiếng Việt được đính kèm trong `fonts/`, cùng giấy phép. Chín hình có bản PDF vector và PNG; LaTeX dùng bản PDF. Biên dịch báo cáo không yêu cầu chạy lại Python.

## Đồng bộ với notebook

Báo cáo dùng output của `../mid_term_code.ipynb`: 70 cell, gồm 41 cell code đã chạy tuần tự, so sánh bốn thuật toán trên năm nhóm đặc trưng. Phụ lục trình bày đủ 20 phương án; các chỉ số khớp output notebook tới bốn chữ số thập phân.

Khi sửa và chạy lại notebook, cần kiểm tra lại các bảng, hình, phiên bản môi trường và mã SHA-256 trong phần Reproducibility của báo cáo. `../Mid-Term.pdf` là đề bài, tách biệt với PDF phân tích này.
