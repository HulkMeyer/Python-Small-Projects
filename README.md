# 🐍 Python Small Projects

A curated collection of small Python projects and assignments spanning data analysis, machine learning, algorithms, math/statistics, and automation. Each project lives in its own folder with its own README and is designed to be self-contained and easy to run.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Projects](https://img.shields.io/badge/Projects-25%2B-orange)

---

## 📁 Repository Structure

```
python-small-projects/
│
├── README.md
├── .gitignore
├── CONTRIBUTING.md
│
├── data-analysis/
│   ├── airbnb-data-cleaning/
│   ├── cereal-numpy-pandas/
│   ├── world-flags-aggregation/
│   ├── harry-potter-wrangling/
│   ├── fandango-movie-ratings/
│   ├── halloween-candy/
│   ├── lego-rebrickable/
│   ├── multiindex-stock-data/
│   ├── data-analysis-examples/
│   ├── dataframe-optimization/
│   ├── pew-research-teen-religion/
│   ├── picture-phrase-numpy/
│   ├── survivor/
│   ├── numpy-pandas-review/
│   └── merging-with-pandas/
│
├── ml-ai/
│   ├── dtsc670-ml-foundations/
│   └── intro-ml-notebooks/
│
└── automation/
    └── python-scripts/
```

---

## 🗂️ Project Index

### 📊 Data Analysis / Visualization

| Project | Description | Key Libraries |
|---------|-------------|---------------|
| [airbnb-data-cleaning](data-analysis/airbnb-data-cleaning/) | Full data cleaning pipeline on Vienna Airbnb listings — missing data, outliers, regex, dummy variables | pandas, numpy, seaborn |
| [cereal-numpy-pandas](data-analysis/cereal-numpy-pandas/) | NumPy & Pandas fundamentals using cereal nutritional data | pandas, numpy, matplotlib |
| [world-flags-aggregation](data-analysis/world-flags-aggregation/) | GroupBy, agg, apply, pivot tables using world flags data | pandas, numpy, scikit-learn |
| [harry-potter-wrangling](data-analysis/harry-potter-wrangling/) | Multi-sheet Excel joining, merging, and concat using Harry Potter character data | pandas, numpy |
| [fandango-movie-ratings](data-analysis/fandango-movie-ratings/) | Replication of FiveThirtyEight's Fandango rating inflation exposé | pandas, numpy, matplotlib |
| [halloween-candy](data-analysis/halloween-candy/) | Data cleaning pipeline on a messy 120-column public survey | pandas, numpy |
| [lego-rebrickable](data-analysis/lego-rebrickable/) | Relational analysis across 12 interconnected LEGO database tables | pandas, numpy |
| [multiindex-stock-data](data-analysis/multiindex-stock-data/) | Multi-index Series and DataFrames using stock ticker price data | pandas, numpy |
| [data-analysis-examples](data-analysis/data-analysis-examples/) | Real-world case studies: Bitly/USA.gov JSON + MovieLens 1M ratings | pandas, numpy, seaborn |
| [dataframe-optimization](data-analysis/dataframe-optimization/) | Benchmarking 6 loop strategies from `iterrows` to NumPy vectorization | pandas, numpy |
| [pew-research-teen-religion](data-analysis/pew-research-teen-religion/) | SPSS survey analysis replicating Pew Research teen religion findings | pandas, pyreadstat |
| [picture-phrase-numpy](data-analysis/picture-phrase-numpy/) | Reverse-engineer NumPy array transformations applied to a hidden image | numpy, matplotlib |
| [survivor](data-analysis/survivor/) | Capstone wrangling assignment using 13-sheet Survivor TV show dataset | pandas, numpy |
| [numpy-pandas-review](data-analysis/numpy-pandas-review/) | Review challenges covering core NumPy and Pandas fundamentals | pandas, numpy |
| [merging-with-pandas](data-analysis/merging-with-pandas/) | Reference notebook: concat, join, and merge with regional sales data | pandas, numpy |

---

### 🤖 ML / AI Experiments

| Project | Description | Key Libraries |
|---------|-------------|---------------|
| [dtsc670-ml-foundations](ml-ai/dtsc670-ml-foundations/) | 8 graded ML assignments: linear/polynomial regression, custom transformers, classification metrics from scratch | scikit-learn, pandas, numpy, matplotlib |
| [intro-ml-notebooks](ml-ai/intro-ml-notebooks/) | Introductory ML: Play Golf binary classifier + Money & Happiness regression | scikit-learn, pandas, numpy |

---

### ⚙️ Automation / Scripting

| Project | Description | Key Libraries |
|---------|-------------|---------------|
| [python-scripts](automation/python-scripts/) | 20+ CLI scripts covering core Python, NumPy, Pandas, and statistical regression | numpy, pandas, statsmodels |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` for package management
- Recommended: [`venv`](https://docs.python.org/3/library/venv.html) or [`conda`](https://docs.conda.io/) for isolated environments

### Running a Project

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/python-small-projects.git
cd python-small-projects

# Navigate to a project
cd data-analysis/airbnb-data-cleaning

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

---

## 🛠️ Common Dependencies

| Library | Purpose |
|---------|---------|
| `numpy` | Numerical computing |
| `pandas` | Data manipulation |
| `matplotlib` / `seaborn` | Visualization |
| `scikit-learn` | Machine learning |
| `statsmodels` | Statistical regression |
| `pyreadstat` | Reading SPSS `.sav` files |
| `openpyxl` | Reading `.xlsx` Excel files |

---

## 📬 Contributing

Have a suggestion or improvement? See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).

---

> Built and maintained by [Christopher Meyer](https://github.com/HulkMeyer)
