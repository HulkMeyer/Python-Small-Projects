# Data Analysis Examples — Real-World Case Studies

> Applied data analysis on real-world datasets from Python for Data Analysis (Wes McKinney), covering JSON parsing, time zone analysis, MovieLens ratings, and comparative approaches using pure Python vs. Pandas.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy%20%7C%20seaborn%20%7C%20matplotlib-orange)

---

## 📌 Overview

This notebook walks through two canonical real-world datasets from Wes McKinney's *Python for Data Analysis*: a 2011 USA.gov/Bitly web analytics snapshot (JSON) and the MovieLens 1M ratings dataset. The primary focus is demonstrating how to approach analysis both in pure Python and with Pandas, emphasizing how Pandas dramatically simplifies common tasks like counting, grouping, and plotting.

---

## 📂 File Structure

```
data-analysis/data-analysis-examples/
├── README.md
├── Data_Analysis_Examples.ipynb
└── datasets/
    ├── bitly_usagov/
    │   └── example.txt
    └── movielens/
        ├── users.dat
        ├── ratings.dat
        └── movies.dat
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy matplotlib seaborn
```

---

## 🚀 How to Run

```bash
cd data-analysis/data-analysis-examples
jupyter notebook Data_Analysis_Examples.ipynb
```

---

## 📋 Topics Covered

**USA.gov / Bitly Dataset:**
- **JSON Parsing** — loading newline-delimited JSON with `json.loads()` and list comprehensions
- **Pure Python Counting** — manual dict-based frequency counting with `get_counts()` and `defaultdict`
- **`collections.Counter`** — elegant built-in shortcut for frequency counting with `most_common()`
- **Pandas `value_counts()`** — one-liner equivalent for the same task
- **Missing Value Cleanup** — `fillna('Missing')` and conditional assignment for empty strings
- **Horizontal Bar Chart** — Seaborn `barplot` for top-10 time zones

**MovieLens 1M Dataset:**
- **`read_csv` with custom separators** — using `sep='::'` for non-standard delimiters
- **Multi-table loading** — users, ratings, and movies in separate files
- **Pivot tables and GroupBy** — computing mean ratings by gender and genre

---

## 💡 Key Concepts

- **Pure Python vs. Pandas** — side-by-side comparison illustrates why Pandas `value_counts()` replaces ~10 lines of manual Python code
- **JSON as a data format** — newline-delimited JSON (NDJSON) is common in web analytics exports; each line is an independent JSON object
- **`Counter.most_common(n)`** — efficient built-in for top-n frequency analysis without sorting manually

---

## 📊 Datasets

**Bitly/USA.gov** (`example.txt`): A 2011 hourly snapshot of anonymized web traffic data from USA.gov shortened URLs, stored as newline-delimited JSON with fields including time zone (`tz`), browser, OS, and URL.

**MovieLens 1M**: 1 million ratings from 6,000 users on 4,000 movies (2003). Spread across three `::` delimited files for users, ratings, and movie metadata.

---

## 🔗 References

- [Python for Data Analysis (McKinney)](https://wesmckinney.com/book/)
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/1m/)
- [collections.Counter Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
