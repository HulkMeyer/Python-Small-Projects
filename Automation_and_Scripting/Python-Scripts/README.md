# Python Scripts — Automation & Fundamentals

> A collection of small command-line Python scripts covering core programming concepts: argument parsing, data structures, string manipulation, NumPy arrays, Pandas DataFrames, statistical regression, and algorithmic problem-solving.

![Category](https://img.shields.io/badge/Category-Automation%20%2F%20Scripting-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-numpy%20%7C%20pandas%20%7C%20statsmodels-orange)

---

## 📌 Overview

A set of standalone Python scripts, each solving a specific programming challenge. All scripts accept command-line arguments via `sys.argv` and are designed to be run from the terminal. Topics range from pure Python fundamentals (loops, sets, dictionaries) to applied data science tasks (OLS regression, logistic regression, random DataFrames).

---

## 📂 File Structure

```
automation/python-scripts/
├── README.md
│
├── # Core Python
├── hello.py
├── luke.py
├── counter.py
├── capCount.py
├── countVowels.py
├── shortest.py
├── palindrome.py
├── inrange.py
├── loopindex.py
├── duckgoose.py
├── duplicates.py
├── commonset.py
├── diffset.py
├── comprehension.py
│
├── # NumPy & Pandas
├── arrayargs.py
├── randdf.py
├── reallyrandom.py
├── presidents.py
│
├── # GPA & Grades
├── gpacalc.py
├── grades.py
│
├── # Statistical Regression
├── fastfood.py
├── german.py
├── sacramento.py
│
└── # Data Files
    ├── fastfood.csv
    ├── german_credit_data.csv
    ├── president_heights.csv
    └── sacramento.csv
```

---

## ⚙️ Requirements

```bash
pip install numpy pandas statsmodels
```

---

## 🚀 How to Run

All scripts are run from the command line with `sys.argv` arguments:

```bash
python luke.py "Leia"
# → Luke, I am your sister

python counter.py "good"
# → {'g': 1, 'o': 2, 'd': 1}

python gpacalc.py A B+ B- C
# → My GPA is 3.08

python fastfood.py
# → OLS regression output for calorie prediction
```

---

## 📋 Script Reference

### Core Python

| Script | Description | Example |
|--------|-------------|---------|
| `hello.py` | Empty starter file | — |
| `luke.py` | Dictionary lookup with special-case logic | `python luke.py "Darth Vader"` → `No, I am your father` |
| `counter.py` | Letter frequency dictionary from a string | `python counter.py "good"` |
| `capCount.py` | Count capitals and sum their indices | `python capCount.py "HeLLo"` |
| `countVowels.py` | Count unique vowels (case-insensitive) | `python countVowels.py "Education"` |
| `shortest.py` | Find shortest word in a string | `python shortest.py "the quick fox"` |
| `palindrome.py` | Check if a string is a palindrome | `python palindrome.py "racecar"` |
| `inrange.py` | Numbers 3000–5000 divisible by n, n+7, n² | `python inrange.py 7` |
| `loopindex.py` | Add each element's index to its value | `python loopindex.py 5 5 5` |
| `duckgoose.py` | Remove all 'goose' entries from a list | `python duckgoose.py duck goose duck` |
| `duplicates.py` | Remove duplicates, sort descending | `python duplicates.py hello world hello` |
| `commonset.py` | Find common words with a fixed reference set | `python commonset.py apple grape mango` |
| `diffset.py` | Find words in input but not in reference set | `python diffset.py grape kiwi apple` |
| `comprehension.py` | Multiply elements divisible by 3 by 10 | `python comprehension.py 1 2 3 4 5 6` |

### NumPy & Pandas

| Script | Description | Example |
|--------|-------------|---------|
| `arrayargs.py` | Build NumPy array from 4 args, print type and product | `python arrayargs.py 2 3 4 5` |
| `randdf.py` | Create random int DataFrame (seed=56) | `python randdf.py 3 4` |
| `reallyrandom.py` | Index into a random array by size/factor/selection | `python reallyrandom.py 10 5 3` |
| `presidents.py` | Average height of sliced presidents | `python presidents.py 0 10` |

### GPA & Grades

| Script | Description | Example |
|--------|-------------|---------|
| `gpacalc.py` | Average GPA for 4 letter grades | `python gpacalc.py A B+ B C` |
| `grades.py` | Average grade excluding one subject | `python grades.py Biology` |

### Statistical Regression

| Script | Description | Output |
|--------|-------------|--------|
| `fastfood.py` | OLS regression: calories ~ fat+sat_fat+cholesterol+sodium | MSE, R², params, p-values |
| `german.py` | OLS regression: credit amount ~ age+duration | params, R² |
| `sacramento.py` | Logistic regression: 1+ bathrooms ~ beds+sqft+price | params, p-values |

---

## 💡 Key Concepts

- **`sys.argv`** — all scripts use `sys.argv[1:]` for command-line input; this is the standard Python pattern for CLI scripts
- **`statsmodels` OLS/Logit** — `sm.OLS()` and `sm.Logit()` with `sm.add_constant()` for intercept; `.fit()` produces model objects with `.params`, `.rsquared`, `.pvalues`
- **Set operations** — `commonset.py` and `diffset.py` demonstrate Python set intersection/difference logic using list comprehensions
- **`np.random.seed()`** — always set before generating random data for reproducibility

---

## 📝 Notes

- `fastfood.py` and `german.py` require their respective CSV files in the same directory
- `presidents.py` requires `president_heights.csv`
- `sacramento.py` requires `sacramento.csv`
- `hello.py` is an intentionally empty starter file

---

## 🔗 References

- [sys.argv Documentation](https://docs.python.org/3/library/sys.html#sys.argv)
- [statsmodels OLS Documentation](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html)
- [statsmodels Logit Documentation](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html)
