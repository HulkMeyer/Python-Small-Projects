# Halloween Candy — Data Cleaning & Wrangling Assignment

> A comprehensive data cleaning pipeline applied to a messy public survey dataset of Halloween candy preferences, preparing it for a machine learning classification model.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)
![Course](https://img.shields.io/badge/Course-DTSC%20580-lightgrey)

---

## 📌 Overview

This assignment applies real-world data cleaning skills to a public Halloween candy survey with 120+ columns and 2,400+ respondents. The goal is to wrangle the raw survey data into a clean, ML-ready DataFrame — handling encoding issues, duplicate detection, column removal, missing value analysis, and categorical preparation — with the target variable being respondent gender.

---

## 📂 File Structure

```
data-analysis/halloween-candy/
├── README.md
├── halloween_candy.ipynb
└── candy.csv
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

```bash
cd data-analysis/halloween-candy
jupyter notebook halloween_candy.ipynb
```

`candy.csv` must be in the same directory as the notebook.

---

## 📋 Topics Covered

- **Encoding Issues** — importing with `encoding='iso-8859-1'` for special characters in public survey data
- **Column Name Cleaning** — replacing malformed characters (`Õ` → `'`) across all column names using `str.replace()`
- **Duplicate Detection** — identifying exact row duplicates vs. duplicates by `Internal ID`
- **Dropping Duplicates** — `drop_duplicates(subset=...)` with default keep-first behavior
- **Column Removal** — dropping irrelevant columns including free-text fields and coordinate data
- **Missing Value Analysis** — counting NaNs in target column (`Q2: GENDER`)
- **`info()` with `max_cols`** — overriding Pandas truncation for wide DataFrames

---

## 💡 Key Concepts

- **Public Survey Data** — real survey exports are messy: encoding artifacts, free-text fields, duplicate submissions, and sparse responses are common
- **Duplicate Definition Matters** — exact duplicates vs. same-ID duplicates can give very different counts
- **Target Variable Quality** — analyzing missingness in the label column before any modeling

---

## 📊 Dataset

`candy.csv` is derived from a public Halloween candy preference survey with 120+ columns covering candy joy/despair ratings, demographic questions (age, gender, country), and free-text comment fields. The classification target is respondent gender (`Q2: GENDER`).

---

## 📝 Notes

- This is a **CodeGrade assignment** — the `candy` DataFrame is progressively updated in place throughout the notebook
- The final cleaned DataFrame shape should be `(2460, 113)`
- The `pd.set_option('display.max_columns', 20)` setting must not be changed as it affects CodeGrade grading

---

## 🔗 References

- [Pandas `drop_duplicates` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)
- [Python `str.replace()` for Column Cleaning](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html)
