"""Build the 14-slide midterm presentation from the reviewed analysis snapshot.

Run from any directory: python slides/build_slides.py
Uses the existing report figures and bundled cover fonts; never trains a model.
After changing notebook outputs, review all numeric statements before rebuilding.
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "presentation_midterm.pdf"
W, H = 960, 540
NAVY = colors.HexColor("#17334C")
TEAL = colors.HexColor("#087F8C")
INK = colors.HexColor("#193246")
MUTED = colors.HexColor("#526474")
BG = colors.HexColor("#F7F9FB")
PALE = colors.HexColor("#E5F1F2")
WHITE = colors.white
GOLD = colors.HexColor("#E8B86D")
FONT = "Helvetica"
BOLD = "Helvetica-Bold"
pdfmetrics.registerFont(TTFont("Names", str(ROOT / "report/fonts/LiberationSerif-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NamesBold", str(ROOT / "report/fonts/LiberationSerif-Bold.ttf")))
c = canvas.Canvas(str(OUT), pagesize=(W, H), invariant=1)
c.setTitle("Book Rating Classification — Midterm Presentation")
c.setAuthor("Lương Văn Thái Tuấn; Nguyễn Thị Khánh Hòa")
c.setSubject("Assignment 6 | Data Analysis with Python | 14 slides")
c.setCreator("slides/build_slides.py (ReportLab)")
page_no = 0


def rect(x, y, w, h, color, radius=0):
    c.setFillColor(color)
    if radius:
        c.roundRect(x, y, w, h, radius, fill=1, stroke=0)
    else:
        c.rect(x, y, w, h, fill=1, stroke=0)


def text(s, x, y, size=18, color=INK, bold=False, font=None):
    f = font or (BOLD if bold else FONT)
    assert pdfmetrics.stringWidth(s, f, size) <= W - x - 28, s
    c.setFillColor(color)
    c.setFont(f, size)
    c.drawString(x, y, s)


def paragraph(s, x, top, width, size=18, color=INK, bold=False, max_height=400):
    style = ParagraphStyle("body", fontName=BOLD if bold else FONT, fontSize=size,
                           leading=size * 1.35, textColor=color, spaceAfter=0)
    p = Paragraph(s, style)
    _, h = p.wrap(width, max_height)
    assert h <= max_height, (s, h, max_height)
    assert top-h >= 43, (s, top-h)
    p.drawOn(c, x, top-h)
    return h


def bullets(items, x, top, width, size=18, gap=13):
    for item in items:
        rect(x, top-size*.65, 5, 5, TEAL)
        h = paragraph(item, x+18, top, width-18, size)
        top -= h + gap
    return top


def photo(path, x, y, w, h):
    path = ROOT / path
    with Image.open(path) as im:
        iw, ih = im.size
    scale = min(w/iw, h/ih)
    dw, dh = iw*scale, ih*scale
    c.drawImage(str(path), x+(w-dw)/2, y+(h-dh)/2, dw, dh, mask="auto")


def frame(title, section, source):
    global page_no
    page_no += 1
    rect(0, 0, W, H, BG)
    rect(0, H-7, W, 7, TEAL)
    text(section.upper(), 44, 499, 10, TEAL, True)
    text(title, 44, 457, 29, NAVY, True)
    rect(44, 437, 872, 1, colors.HexColor("#D9E2E9"))
    text("BOOK RATING CLASSIFICATION", 44, 19, 8, MUTED)
    text(source, 245, 19, 8, MUTED)
    text(f"{page_no:02d} / 14", 871, 19, 9, MUTED)


def end():
    c.showPage()


def card(x, y, w, value, label, detail="", color=TEAL):
    rect(x, y, w, 135, WHITE, 9)
    rect(x, y+125, w, 10, color, 3)
    text(value, x+20, y+78, 32, color, True)
    paragraph(label, x+20, y+58, w-40, 16, INK, True, 45)
    if detail:
        paragraph(detail, x+20, y+27, w-40, 11, MUTED, max_height=30)


def table(headers, rows, widths, x=44, top=402, row_h=42, size=17, highlight=None):
    assert sum(widths) <= 872
    rect(x, top-row_h, sum(widths), row_h, NAVY, 4)
    left = x
    for head, width in zip(headers, widths):
        text(head, left+12, top-row_h+15, size-1, WHITE, True)
        left += width
    y = top-row_h
    for i, row in enumerate(rows):
        rect(x, y-row_h, sum(widths), row_h, PALE if i==highlight else (WHITE if i%2==0 else BG))
        left=x
        for entry, width in zip(row, widths):
            entry=str(entry)
            f = BOLD if i==highlight else FONT
            assert pdfmetrics.stringWidth(entry, f, size) < width-20, (entry, width)
            text(entry, left+12, y-row_h+15, size, TEAL if i==highlight else INK, i==highlight)
            left += width
        y -= row_h
    return y


# 01 | Cover
page_no += 1
rect(0, 0, W, H, NAVY)
rect(0, 0, 16, H, TEAL)
rect(731, 0, 229, H, colors.HexColor("#20445D"))
rect(756, 332, 174, 171, WHITE, 10)
photo("report/neu_logo.png", 763, 416, 160, 81)
photo("report/fda_logo.png", 794, 343, 100, 71)
text("NATIONAL ECONOMICS UNIVERSITY", 48, 491, 15, WHITE, True)
paragraph("Faculty of Data Science and Artificial Intelligence", 48, 475, 635, 13, colors.HexColor("#CEE0EA"))
text("DATA ANALYSIS WITH PYTHON  /  ASSIGNMENT 06", 48, 401, 11, GOLD, True)
text("Book Rating", 48, 331, 52, WHITE, True)
text("Classification", 48, 270, 52, WHITE, True)
paragraph("Can user and book information help identify<br/>ratings of 8–10?", 51, 230, 650, 23, colors.HexColor("#CEE0EA"))
text("Lương Văn Thái Tuấn — 11258665", 51, 124, 19, WHITE, font="Names")
text("Nguyễn Thị Khánh Hòa — 11253156", 51, 98, 19, WHITE, font="Names")
text("Supporting lecturer: Dr. Trần Đức Minh", 51, 64, 18, WHITE, font="Names")
text("2 NOVEMBER 2026", 770, 52, 11, WHITE, True)
text("01 / 14", 871, 19, 9, WHITE)
end()

# 02 | Problem
frame("Predict the rating class, one rating at a time", "01 / Problem", "Source: notebook §0; report §1")
card(44, 270, 280, "8–10", "Class 1: high rating", "Threshold selected by the group")
card(340, 270, 280, "1–7", "Class 0: other ratings", "Does not mean the reader dislikes it")
card(636, 270, 280, "0", "Implicit feedback", "Retained for activity summaries", color=MUTED)
bullets([
    "Prediction unit: one observed user–book rating with a score from 1 to 10.",
    "Inputs: user and book metadata plus statistics from other training ratings.",
    "Scope: binary classification; these metrics do not evaluate recommendation ranking."
], 52, 229, 850, 20, 17)
end()

# 03 | Dataset
frame("Three tables, linked through users and books", "02 / Data", "Data: Möbius / Kaggle; notebook §1–2")
c.linkURL("https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset",
          (245, 15, 490, 30), relative=0)
table(["Table", "Raw rows", "Key / content"], [
    ["Books", "271,360", "ISBN; title, author, year, publisher"],
    ["Users", "278,858", "User-ID; location, age"],
    ["Ratings", "1,149,780", "User-ID + ISBN; score 0–10"],
], [155, 180, 537], row_h=49)
paragraph("Ratings join Users on User-ID   |   Ratings join Books on ISBN", 58, 181, 840, 21, TEAL, True)
bullets([
    "Left joins preserve ratings even when book metadata are unavailable.",
    "Many-to-one validation prevents row multiplication; ISBN stays a string."
], 55, 132, 850, 18, 10)
end()

# 04 | Cleaning
frame("Clean metadata while preserving the rating sample", "03 / Preparation", "Source: notebook §3; report §3")
bullets([
    "Trim ISBNs; remove one exact duplicate book row after normalization.",
    "Quarantine three malformed book rows; retain their associated ratings.",
    "Age rule: 5–100. Publication-year rule: 1450–2026; year 0 means unknown.",
    "Keep missingness flags; learn numeric medians inside the training pipeline."
], 48, 400, 860, 19, 15)
card(44, 65, 280, "433,671", "Explicit ratings", "Final classification dataset")
card(340, 65, 280, "30.11%", "Age missing", "Among classification ratings")
card(636, 65, 280, "11.49%", "Book metadata missing", "49,829 classification ratings")
end()

# 05 | Rating distribution
frame("High ratings are common; a baseline is essential", "04 / Exploration", "Source: notebook §4.2; report §4.1–4.2")
photo("report/figures/03_phan_phoi_diem_en.png", 30, 85, 590, 335)
text("57.62%", 650, 355, 42, TEAL, True)
paragraph("of explicit ratings<br/>belong to class 1", 650, 330, 270, 20, INK, True)
bullets([
    "249,887 high ratings; 183,784 ratings of 1–7.",
    "Score 8 is the most frequent explicit score.",
    "Always predicting class 1 already gives 57.62% Accuracy."
], 638, 256, 280, 17, 15)
end()

# 06 | EDA insight
frame("Activity is uneven, and age alone is a weak signal", "04 / Exploration", "Source: notebook §4.6–4.8; report §4.3–4.4")
photo("report/figures/05_tuoi_va_hoat_dong_en.png", 37, 121, 530, 297)
bullets([
    "Known user age: median 32; age is missing for 40.17% of all users.",
    "Age-group / rating-class association is small: Cramér’s V is about 0.0483.",
    "User rating counts are highly uneven; test count and ID-rate features."
], 592, 399, 319, 18, 19)
rect(44, 59, 872, 52, PALE, 6)
paragraph("Repeated users and books violate simple independence assumptions; EDA is descriptive, not causal evidence.", 60, 98, 840, 17, TEAL, max_height=44)
end()

# 07 | Split
frame("Separate fitting, selection and evaluation", "05 / Experiment design", "Source: notebook §5.2–5.5; report §5")
card(44, 266, 280, "70%", "Train: 303,569", "Fit preprocessing and estimators")
card(340, 266, 280, "15%", "Validation: 65,051", "Select one of 20 configurations")
card(636, 266, 280, "15%", "Test: 65,051", "Evaluate the selected pipeline")
bullets([
    "Stratify by class; split seed 56. Same partitions for every configuration.",
    "Imputation, scaling and one-hot encoding learn only from train.",
    "Validation/test count and rate features look up train statistics only.",
    "Train target rates use 5-fold OOF encoding and smoothing (alpha = 20)."
], 52, 231, 852, 18, 11)
end()

# 08 | Features
frame("Five cumulative feature groups", "06 / Feature engineering", "Source: notebook §5.1–5.5; report §5.1, §5.3")
table(["Group", "New information", "Inputs"], [
    ["Initial", "Age, publication year, missingness flags", "4"],
    ["Metadata", "Book author and publisher", "6"],
    ["Country", "Country parsed from Location", "7"],
    ["Count", "Training rating counts per user / book", "9"],
    ["Target Encoding", "OOF high-rating rates per user / book", "11"],
], [205, 560, 107], row_h=43, size=17, highlight=4)
paragraph("Book-Rating is excluded from X. User-ID and ISBN are lookup keys, not numeric predictors.", 57, 119, 842, 19, TEAL, True)
paragraph("Unseen IDs: count = 0; target rate = training prior. OOF excludes each row’s own label.", 57, 67, 842, 15, MUTED)
end()

# 09 | Algorithms and selection
frame("20 configurations; one selection rule", "07 / Modeling", "Source: notebook §5.3–5.6; report §6")
table(["Algorithm", "Fixed configuration across feature groups"], [
    ["Logistic Regression", "Balanced class weights; max_iter = 1000"],
    ["Decision Tree", "Balanced; depth 20; minimum leaf size 50"],
    ["Linear SVM", "Balanced; LinearSVC; max_iter = 3000"],
    ["MLP", "Hidden layers (64, 32); training-loss stopping"],
], [266, 606], row_h=44, size=17)
rect(44, 77, 872, 83, NAVY, 7)
paragraph("Select the highest validation Macro F1", 65, 144, 825, 23, WHITE, True)
paragraph("Tie-break: ROC-AUC, then Accuracy. Baseline: always predict the majority class.", 65, 106, 825, 17, colors.HexColor("#CEE0EA"))
end()

# 10 | Validation
frame("Target encoding gives the clearest gains", "08 / Validation results", "Source: notebook §5.6; report §7")
photo("report/figures/07_so_sanh_macro_f1_validation_en.png", 35, 99, 620, 319)
text("0.6597", 675, 356, 39, TEAL, True)
paragraph("Validation Macro F1<br/><b>LR + Target Encoding</b>", 675, 334, 245, 18)
bullets([
    "LR Count: 0.5638<br/>LR Target Encoding: 0.6597",
    "SVM is close: 0.6594. A single split does not establish a stable advantage."
], 663, 242, 253, 17, 16)
paragraph("Selected across all 20 configurations using the same validation criterion.", 58, 73, 843, 18, TEAL, True)
end()

# 11 | Test comparison
frame("Better recognition of both classes, with trade-offs", "09 / Test results", "Source: notebook §5.7; report §8.1")
table(["Metric", "LR + Target Encoding", "Baseline"], [
    ["Accuracy", "0.6565", "0.5762"],
    ["Macro F1", "0.6553", "0.3656"],
    ["ROC-AUC", "0.7306", "0.5000"],
    ["Class 0 Recall", "0.7041", "0.0000"],
    ["Class 1 F1", "0.6758", "0.7311"],
], [316, 326, 230], row_h=40, highlight=1)
text("+8.03 pp Accuracy", 61, 124, 24, TEAL, True)
text("+0.2897 Macro F1", 504, 124, 24, TEAL, True)
paragraph("Class 1 F1 falls versus the baseline. The selected model does not lead on every metric.", 59, 91, 846, 17, MUTED)
end()

# 12 | Confusion and ROC
frame("Errors and discrimination on 65,051 test ratings", "09 / Test results", "Source: notebook §5.7–5.8; report §8.2–8.3")
photo("report/figures/08_confusion_matrix_test_en.png", 42, 140, 420, 279)
photo("report/figures/09_roc_test_en.png", 496, 140, 420, 279)
paragraph("<b>High-rating precision: 74.07%</b><br/>23,294 correct out of 31,450 high predictions.", 51, 117, 410, 17)
paragraph("<b>ROC-AUC: 0.7306</b><br/>Discrimination across thresholds; not Accuracy or a calibration measure.", 503, 117, 410, 17)
end()

# 13 | Segments
frame("Aggregate performance does not cover every ID group", "10 / Generalization", "Source: notebook §5.7; report §8.4")
table(["Test segment", "Ratings", "Macro F1", "Recall 1"], [
    ["Seen user, seen book", "37,143", "0.6589", "0.6609"],
    ["New user, seen book", "5,513", "0.5673", "0.4963"],
    ["Seen user, new book", "19,908", "0.6832", "0.6361"],
    ["New user, new book", "2,487", "0.4234", "0.1097"],
], [398, 145, 166, 163], row_h=47, size=17, highlight=3)
bullets([
    "Both IDs new: rate features fall back to the prior; count features equal zero.",
    "Segments have different class mix and sample sizes. Use an ID-based split for stronger evidence."
], 54, 134, 848, 18, 13)
end()

# 14 | Conclusion
frame("A useful signal, with a clear next validation step", "11 / Conclusions", "Source: notebook §6; report §9–10")
rect(44, 249, 422, 165, WHITE, 8)
rect(485, 249, 431, 165, WHITE, 8)
text("WHAT WE LEARNED", 64, 383, 14, TEAL, True)
bullets([
    "Training rating tendencies improve this classification experiment.",
    "LR + Target Encoding leads validation; test Macro F1 is 0.6553."
], 63, 358, 380, 18, 13)
text("WHAT REMAINS LIMITED", 505, 383, 14, TEAL, True)
bullets([
    "Random rating split shares IDs; missing metadata and OOF shift remain.",
    "EDA used the full sample; test was already viewed during development."
], 505, 358, 388, 18, 13)
paragraph("Next: a fresh holdout, user/book or time-based evaluation, repeated splits, and ranking metrics before recommendation use.", 59, 217, 842, 20, INK, True)
paragraph("Materials: notebook + analysis report + this 14-slide presentation", 59, 117, 842, 18, TEAL)
url="https://github.com/Bluenip/Data_analyst_python_midterm_project"
text("github.com/Bluenip/Data_analyst_python_midterm_project", 59, 62, 15, MUTED)
c.linkURL(url, (59, 56, 760, 78), relative=0)
end()
assert page_no == 14
c.save()
print(f"Built {page_no} slides: {OUT}")
