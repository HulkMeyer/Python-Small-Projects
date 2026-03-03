# Pew Research 2019 — US Teens & Religion Survey Analysis

> An exploratory analysis of a 2019 Pew Research Center survey on US teen religiosity, loading SPSS `.sav` data directly into Pandas and replicating published findings about parent-child religious alignment.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy%20%7C%20pyreadstat-orange)

---

## 📌 Overview

This notebook replicates analysis from Pew Research's 2020 publication *"U.S. Teens Take After Their Parents Religiously"* using the underlying 2019 survey microdata. It demonstrates loading SPSS-format data (`.sav`) directly into Pandas, navigating a codebook-driven dataset, and using `groupby` and filtering to reproduce published statistics about parent-child religious denomination matching.

---

## 📂 File Structure

```
data-analysis/pew-research-teen-religion/
├── README.md
├── PewRel2019_StudentTemplate.ipynb
└── US_Teens_and_their_parents_-_2019_Pew_Research_Survey_-_FOR_RELEASE.sav
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy pyreadstat
```

`pyreadstat` is required to read SPSS `.sav` files via `pd.read_spss()`.

---

## 🚀 How to Run

```bash
cd data-analysis/pew-research-teen-religion
jupyter notebook PewRel2019_StudentTemplate.ipynb
```

The `.sav` file must be in the same directory as the notebook.

---

## 📋 Topics Covered

- **Reading SPSS Files** — `pd.read_spss()` to load `.sav` survey microdata directly into a DataFrame
- **Codebook Navigation** — identifying column names and value encodings from a survey codebook rather than column headers
- **`describe()` for Categoricals** — using `include='all'` to get summary stats for both numeric and categorical columns
- **`value_counts()`** — inspecting response distributions for categorical survey variables
- **Boolean Filtering** — selecting respondents matching compound criteria (e.g., agnostic parent + Catholic teen)
- **`groupby().size().nlargest()`** — finding the most common parent-child denomination combinations
- **Categorical Data Types** — understanding how SPSS-sourced categoricals behave in Pandas

---

## 💡 Key Concepts

- **SPSS `.sav` Format** — common in academic social science research; Pandas can read it via `pyreadstat` without converting to CSV
- **Codebook-Driven Analysis** — variable names in survey data (e.g., `preligrec`, `treltrad`) are cryptic; a codebook is essential for interpreting them
- **Replicating Published Research** — this notebook demonstrates the reproducibility pipeline from raw microdata to published findings

---

## 📊 Dataset

The dataset is a 2019 Pew Research Center survey of US teens and their parents about religious beliefs, practices, and denomination. It is publicly available from [Pew Research Center](https://www.pewresearch.org/religion/2020/09/10/u-s-teens-take-after-their-parents-religiously-attend-services-together-and-enjoy-family-rituals/). Key variables include parent religious tradition (`Preltrad`), teen religious tradition (`treltrad`), parent/teen denomination codes, and demographic attributes.

---

## 🔗 References

- [Pew Research Publication](https://www.pewresearch.org/religion/2020/09/10/u-s-teens-take-after-their-parents-religiously-attend-services-together-and-enjoy-family-rituals/)
- [pyreadstat Documentation](https://github.com/Roche/pyreadstat)
- [Pandas `read_spss` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html)
