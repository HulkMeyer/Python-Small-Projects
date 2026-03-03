# NumPy & Pandas Review Challenges

> Two standalone review notebooks covering fundamental NumPy array operations and Pandas Series/DataFrame skills, structured as practice exercises with auto-graded outputs.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)
![Course](https://img.shields.io/badge/Course-DTSC%20580-lightgrey)

---

## 📌 Overview

Two review notebooks designed to reinforce foundational skills in NumPy and Pandas. Each question builds a variable (`Q1`, `Q2`, etc.) that serves as a checkpoint, with solutions checked against expected outputs. Covers array creation, reshaping, masking, stacking, Series indexing, DataFrame construction, and descriptive statistics.

---

## 📂 File Structure

```
data-analysis/numpy-pandas-review/
├── README.md
├── numpy_review.ipynb
└── pandas_review.ipynb
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

```bash
cd data-analysis/numpy-pandas-review
jupyter notebook numpy_review.ipynb
# or
jupyter notebook pandas_review.ipynb
```

---

## 📋 NumPy Review Topics

- `np.array()`, `np.arange()` — array creation from ranges
- `[::-1]` — reversing array order
- `.reshape()` — converting 1D arrays to 2D matrices
- `np.random.seed()` + `np.random.random()` — reproducible random arrays
- `np.min()`, `np.max()`, `np.mean()` — summary statistics
- Boolean masking — selecting even numbers with `arr[arr%2==0]`
- `np.where()` — conditional value replacement
- `np.vstack()` / `np.hstack()` — vertical and horizontal array stacking

## 📋 Pandas Review Topics

- `pd.Series()` from arrays and dictionaries — with custom index labels
- Index-based filtering — `Q2['c']`, `Q4[Q4 > 2]`
- Series arithmetic with mismatched indexes — NaN propagation behavior
- `.dropna()`, `.name`, `.index.name` — Series cleanup and metadata
- `pd.DataFrame()` from dict — column types and index
- `.assign()` and `del` — adding and removing columns
- Nested dictionary → DataFrame — outer keys as columns, inner keys as row index
- `pd.set_option('display.max_columns', None)` — display configuration

---

## 💡 Key Concepts

- **Views vs. Copies** — `arr.copy()` before modifying to prevent unintended side effects on the original array
- **NaN propagation in Series math** — adding two Series with different indexes produces NaN for non-matching labels
- **`np.where()` vs. boolean masking** — `np.where(condition)` returns indices; boolean masking returns values directly

---

## 📝 Notes

- Both notebooks are **CodeGrade assignments** — each answer is saved as a numbered variable
- `numpy_review.ipynb` uses `np.random.seed(42)` — do not change this or answers will not match
- Some cells include alternate solution approaches in comments for learning purposes

---

## 🔗 References

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
