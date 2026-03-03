# Machine Learning Fundamentals — Golf & Happiness

> Two introductory machine learning notebooks: a binary classifier built with linear regression to predict whether to play golf given weather conditions, and a simple linear regression exploring the relationship between GDP per capita and life satisfaction.

![Category](https://img.shields.io/badge/Category-ML%20%2F%20AI-blueviolet)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-sklearn%20%7C%20pandas%20%7C%20numpy%20%7C%20matplotlib-orange)

---

## 📌 Overview

**Play Golf:** A guided introduction to the ML workflow using weather data. Categorical features are one-hot encoded, a `LinearRegression` model is trained, predictions are threshold-converted to binary labels, and accuracy is computed — all with ~14 rows of data, making every step easy to trace.

**Money & Happiness:** A classic first ML example from *Hands-On Machine Learning* (Géron) — fitting a linear regression to OECD life satisfaction vs. GDP per capita data to explore whether money predicts happiness.

---

## 📂 File Structure

```
ml-ai/ML-Fundamentals/
├── README.md
├── PlayGolfRegression_template.ipynb
├── PlayGolfData.csv
├── module_1_MoneyAndHappiness__1_.ipynb
└── datasets/
    ├── oecd_bli_2015.csv
    └── gdp_per_capita.csv
```

---

## ⚙️ Requirements

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## 🚀 How to Run

```bash
cd ml-ai/intro-ml-notebooks
jupyter notebook PlayGolfRegression_template.ipynb
# or
jupyter notebook module_1_MoneyAndHappiness__1_.ipynb
```

---

## 📋 Topics Covered

**Play Golf:**
- `pd.get_dummies(drop_first=True)` for one-hot encoding of `Outlook`, `Windy`, `Play`
- `LinearRegression.fit()`, `.coef_`, `.intercept_`
- `itertuples()` for row-wise prediction
- List comprehension with threshold: `[1 if x >= 0.5 else 0 for x in outputs]`
- `accuracy_score()` evaluation

**Money & Happiness:**
- Data preparation pipeline function for merging OECD and GDP data
- `sklearn.linear_model.LinearRegression` fit and predict
- Scatter plot of GDP vs. life satisfaction with regression line overlay

---

## 💡 Key Concepts

- **Linear Regression as Classifier** — applying a cutoff (0.5) to continuous regression outputs creates binary predictions; this conceptually bridges to logistic regression
- **One-Hot Encoding with `drop_first`** — dropping one dummy variable prevents multicollinearity in OLS-based methods
- **`itertuples()` for prediction** — more efficient than `iterrows()` for row-by-row `predict()` calls during evaluation

---

## 🔗 References

- [Hands-On Machine Learning (Géron)](https://github.com/ageron/handson-ml2)
- [scikit-learn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
