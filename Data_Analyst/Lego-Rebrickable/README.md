# LEGO Rebrickable — Multi-Table Relational Data Analysis

> A relational database-style analysis of the complete LEGO parts catalog using 12 interconnected CSV tables from the Rebrickable dataset, applying merges, aggregations, and custom functions to answer real-world inventory questions.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20numpy-orange)
![Course](https://img.shields.io/badge/Course-DTSC%20580-lightgrey)

---

## 📌 Overview

This assignment loads 12 relational CSV tables from the [Rebrickable](https://rebrickable.com/) LEGO database and performs multi-table analysis to answer questions about LEGO sets, parts, themes, colors, and minifigures. Students must determine which tables to join and how, mirroring the experience of working with a real relational database schema.

---

## 📂 File Structure

```
data-analysis/lego-rebrickable/
├── README.md
├── lego.ipynb
├── Lego_Schema.png
├── inventories.csv
├── inventory_sets.csv
├── inventory_parts.csv
├── inventory_minifigs.csv
├── sets.csv
├── themes.csv
├── minifigs.csv
├── parts.csv
├── part_categories.csv
├── part_relationships.csv
├── colors.csv
└── elements.csv
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

```bash
cd data-analysis/lego-rebrickable
jupyter notebook lego.ipynb
```

All CSV files and `Lego_Schema.png` must be in the same directory as the notebook.

---

## 📋 Topics Covered

- **Multi-Table Schema Navigation** — understanding foreign key relationships across 12 tables (see `Lego_Schema.png`)
- **Exploratory Analysis** — `head()`, `info()`, `describe()` across all tables before merging
- **Custom Functions** — writing reusable functions (e.g., `data_count`) that accept a DataFrame and return computed values
- **Descriptive Statistics** — average and median parts per set, identifying skew from high-part outlier sets
- **Multi-Table Merges** — joining inventories → sets → themes → parts → colors as needed per question
- **Aggregation** — groupby operations for counts, sums, and averages across LEGO themes, years, and categories
- **Selective Table Usage** — determining which of the 12 tables are relevant for each specific question

---

## 💡 Key Concepts

- **Relational Schema** — the `Lego_Schema.png` diagram is essential context; tables connect through `inventory_id`, `set_num`, `part_num`, `color_id`, and `fig_num` foreign keys
- **Mean vs. Median** — the median parts per set is much lower than the mean, indicating a right-skewed distribution driven by large collector sets
- **Data Relevance** — not all 12 tables are needed for every question; choosing the right tables is a core data science skill

---

## 📊 Dataset

All data sourced from [Rebrickable](https://rebrickable.com/downloads/), which provides a complete catalog of LEGO sets, parts, colors, themes, and minifigures. As of the dataset snapshot, there are 18,576 LEGO sets represented.

| Table | Description |
|-------|-------------|
| `sets` | Set name, year, theme, part count |
| `themes` | Theme hierarchy with parent IDs |
| `inventories` | Version tracking per set |
| `inventory_parts` | Parts per inventory with color and quantity |
| `parts` | Part catalog with categories |
| `colors` | Color names, RGB values, transparency |
| `minifigs` | Minifigure catalog |
| `inventory_minifigs` | Minifigs included per inventory |
| `elements` | Element IDs linking parts to colors |

---

## 📝 Notes

- This is a **CodeGrade assignment** with auto-graded function outputs
- The `pd.set_option('display.max_columns', None)` setting must not be changed
- The schema diagram (`Lego_Schema.png`) should be referenced before writing any merge logic

---

## 🔗 References

- [Rebrickable Database Downloads](https://rebrickable.com/downloads/)
- [Pandas Merge Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
