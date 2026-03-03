# Survivor — Comprehensive Data Wrangling Assignment

> A full-course capstone assignment applying data manipulation skills to the TV show Survivor dataset — combining multi-sheet Excel imports, snake_case normalization, merging, filtering, groupby aggregation, and sorting to answer statistical questions about 40+ seasons of competition.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)
![Course](https://img.shields.io/badge/Course-DTSC%20580-lightgrey)

---

## 📌 Overview

This capstone assignment uses real Survivor TV show data spread across 13 Excel sheets to test all data manipulation skills from the course. Students import multiple sheets, normalize all column names to snake_case, and then answer analytical questions: oldest contestant, most seasons played, sole survivors, two-time winners, average age, most days played, and more.

---

## 📂 File Structure

```
data-analysis/survivor/
├── README.md
├── survivor.ipynb
└── survivor.xlsx         ← 13 sheets of Survivor data
```

**Excel Sheets:** `Castaway Details`, `Castaways`, `Challenge Description`, `Challenge Results`, `Confessionals`, `Hidden Idols`, `Jury Votes`, `Tribe Mapping`, `Viewers`, `Vote History`, `Season Summary`, `Season Palettes`, `Tribe Colours`

---

## ⚙️ Requirements

```bash
pip install pandas numpy openpyxl
```

---

## 🚀 How to Run

```bash
cd data-analysis/survivor
jupyter notebook survivor.ipynb
```

`survivor.xlsx` must be in the same directory as the notebook.

---

## 📋 Topics Covered

- **Multi-Sheet Excel Import** — `pd.ExcelFile()` + `pd.read_excel()` for each of 13 sheets
- **Bulk Column Renaming** — using a `for` loop with `lambda col: col.replace(' ', '_').lower()` across all DataFrames at once
- **Snake_case Convention** — standardizing column names for easier programmatic access
- **Boolean Filtering** — `castaways[castaways['age'] == max_age]` to find oldest contestant
- **`value_counts()`** — identifying contestants with the most season appearances
- **`sort_values()` + `reset_index()`** — creating sorted, cleanly indexed result DataFrames
- **Multi-Season Winners** — detecting contestants who won more than once using `value_counts()` on `castaway_id`
- **`groupby()` + `sum()`** — aggregating total days played across multiple seasons per contestant
- **`merge()` across sheets** — joining `castaways` with `castaway_details` for full contestant profiles
- **`nlargest()`** — selecting top-n rows by a column value

---

## 💡 Key Concepts

- **Snake_case normalization** — a standard first step; `col.replace(' ', '_').lower()` applied via `rename(columns=lambda...)` is cleaner than manual renaming
- **Multi-sheet analysis** — not all sheets are needed for every question; choosing which to merge is a core analytical decision
- **Contestant vs. Season records** — `castaways` has one row per season-appearance while `castaway_details` has one row per person; joining them correctly requires understanding the grain

---

## 📊 Dataset

A real dataset from the `survivoR` R package covering all seasons of the CBS TV show Survivor. Includes castaway demographics, challenge results, vote history, confessional counts, jury votes, tribal assignments, and viewership data.

---

## 📝 Notes

- This is a **CodeGrade assignment** with auto-graded question outputs (`Q2`, `Q3`, etc.)
- The `pd.set_option('display.max_columns', None)` setting must not be changed
- You may or may not need all 13 sheets — deciding which to use is part of the exercise

---

## 🔗 References

- [survivoR R Package (Data Source)](https://github.com/doehm/survivoR)
- [Pandas Multi-Sheet Excel Import](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html)
