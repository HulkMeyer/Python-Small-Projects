# DataFrame Loop Optimization

> A performance benchmarking study comparing five approaches to row-wise DataFrame operations in Pandas — from basic Python loops to NumPy vectorization — using `%%timeit` to measure real execution times on 100,000 rows.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)

---

## 📌 Overview

A common beginner mistake in data science is using slow Python loops on DataFrames. This notebook benchmarks five progressively faster approaches to the same task — mapping 100,000 review scores to star ratings — using Jupyter's `%%timeit` magic. Results clearly demonstrate why vectorized operations are preferred in production data pipelines.

---

## 📂 File Structure

```
data-analysis/dataframe-optimization/
├── README.md
└── Optimization.ipynb
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

```bash
cd data-analysis/dataframe-optimization
jupyter notebook Optimization.ipynb
```

> ⚠️ **Note:** The basic Python loop cell (`basic_loop`) is intentionally commented out — it is extremely slow on 100,000 rows and would hang the kernel.

---

## 📋 Approaches Benchmarked

| Method | Description | Relative Speed |
|--------|-------------|---------------|
| Basic `for` loop | Iterates with integer index | Slowest (skip) |
| `iterrows()` | Yields `(index, Series)` tuples | Very slow |
| `apply()` + lambda | Row-wise function application | Moderate |
| `itertuples()` | Yields named tuples (faster than `iterrows`) | Faster |
| `np.where()` | Nested conditional vectorization | Fast |
| Pandas vectorization | `.loc`-based bulk assignment | Very fast |
| NumPy vectorization | Direct array operations | Fastest |

---

## 💡 Key Concepts

- **`iterrows()` dtype loss** — `iterrows()` converts each row to a Series, which can silently change dtypes; `itertuples()` preserves types and is faster
- **`%%timeit`** — Jupyter magic that runs a cell multiple times and reports mean ± std execution time; essential for benchmarking
- **Vectorization** — operating on entire arrays at once instead of element-by-element; NumPy and Pandas are optimized for this at the C level
- **`np.where()`** — elegant nested conditional that avoids any Python-level looping

---

## 📝 Notes

- The basic loop cell is commented with `#%%timeit` — running it would take extremely long and is advised to skip
- All approaches produce the same output; the comparison is purely about execution speed
- The 100,000-row synthetic DataFrame uses `np.random.seed(42)` for reproducibility

---

## 🔗 References

- [Pandas `iterrows` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)
- [Pandas `itertuples` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html)
- [Stack Overflow: What is Vectorization?](https://stackoverflow.com/questions/1422149/what-is-vectorization)
