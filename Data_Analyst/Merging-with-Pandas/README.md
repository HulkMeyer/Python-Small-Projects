# Merging with Pandas — Regional Sales

> A focused reference notebook demonstrating `concat`, `join`, and `merge` using a regional sales dataset with Eastern/Western region data, sales teams, store info, and product tables.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)

---

## 📌 Overview

A concise reference notebook illustrating the three primary Pandas combining methods — `concat`, `join`, and `merge` — using a realistic regional sales dataset. The notebook demonstrates when to use each method, what the different join types (`inner`, `left`, `right`, `outer`) produce, and how to handle column conflicts with suffixes.

---

## 📂 File Structure

```
data-analysis/merging-with-pandas/
├── README.md
├── Merging_with_Pandas_Jupyter_Notebook.ipynb
└── Regional_Sales.xlsx         ← 5 sheets: eastern_region, western_region, sales_team, store_name, store_info, product
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy openpyxl
```

---

## 🚀 How to Run

```bash
cd data-analysis/merging-with-pandas
jupyter notebook Merging_with_Pandas_Jupyter_Notebook.ipynb
```

---

## 📋 Topics Covered

- **`pd.concat()`** — stacking Eastern and Western region rows; `ignore_index=True` to reset index
- **`join()`** — column-wise joining of `store_name` and `store_info` on index; equivalent to `pd.concat(axis=1)`
- **`merge()`** — inner, left, right, and outer joins with `sales_team` and `product` tables
- **Merge on specific columns** — `sales.merge(store, on='StoreID')`
- **Join type comparison** — visual demonstration of how row counts change with each join type

---

## 📊 Dataset

`Regional_Sales.xlsx` is a synthetic sales dataset with sheets for Eastern region, Western region, sales team assignments, store names, store info, and product details.

---

## 🔗 References

- [Pandas `concat` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
- [Pandas `merge` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
