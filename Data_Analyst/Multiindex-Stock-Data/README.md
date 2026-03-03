# Multi-Index with Stock Data

> An introduction to Pandas multi-indexing using a stock price dataset, covering hierarchical index creation, partial indexing, sorting, stacking/unstacking, and cross-sectional selection across multiple ticker symbols.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)

---

## 📌 Overview

This notebook introduces Pandas multi-indexing — a powerful but often underutilized feature for working with hierarchical data. Using stock price data indexed by both ticker symbol and date, the notebook covers partial indexing, slicing, sorting multi-index Series, and reshaping between long and wide formats. Key stocks analyzed include AAPL, AMZN, BAC, and WFC.

---

## 📂 File Structure

```
data-analysis/multiindex-stock-data/
├── README.md
├── MultiIndex_with_Stock_Data_Student_Template.ipynb
└── stock.csv
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

```bash
cd data-analysis/multiindex-stock-data
jupyter notebook MultiIndex_with_Stock_Data_Student_Template.ipynb
```

`stock.csv` must be in the same directory as the notebook.

---

## 📋 Topics Covered

- **Creating a Multi-Index** — using `index_col=['Stock', 'Date']` when reading CSV to set a two-level index
- **Multi-Index Series** — constructing from a nested list of index arrays
- **Partial Indexing** — selecting data for a single outer-level key (e.g., all AAPL rows)
- **Range Indexing** — slicing from one ticker to another with sorted multi-index
- **Inner-Level Indexing** — using `.loc[:, value]` to select across all outer keys
- **`sort_index()`** — required before range-based indexing on unsorted multi-indexes
- **`unstack()`** — converting a multi-index Series to a wide-format DataFrame
- **`stack()`** — converting a wide DataFrame back to a multi-index Series
- **Basic Stock Statistics** — min, max, mean price per ticker

---

## 💡 Key Concepts

- **Why Multi-Index?** — enables compact, efficient representation of panel data (multiple entities observed over time) without duplicating index columns
- **Sort Before Slice** — range indexing on a multi-index raises a `PerformanceWarning` or returns unexpected results if the index is not sorted first
- **`unstack()` fills NaN** — when converting to wide format, missing combinations of index levels are filled with NaN

---

## 📊 Dataset

`stock.csv` contains daily closing price data for multiple stock tickers indexed by stock symbol and date. Tickers include major stocks such as AAPL (Apple), AMZN (Amazon), BAC (Bank of America), and WFC (Wells Fargo).

---

## 🔗 References

- [Pandas Multi-Index Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)
- [Pandas `stack` / `unstack` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html)
