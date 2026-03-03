# ML Regression-Pipeline

> A progressive series of machine learning assignments covering linear regression, data pipelines, custom transformers, classification metrics, and polynomial regression — implemented from scratch and validated against scikit-learn.

![Category](https://img.shields.io/badge/Category-ML%20%2F%20AI-blueviolet)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-sklearn%20%7C%20pandas%20%7C%20numpy%20%7C%20matplotlib-orange)
![Course](https://img.shields.io/badge/Course-DTSC%20670-lightgrey)

---

## 📌 Overview

Eight graded assignments from DTSC670 (Foundations of Machine Learning Models) that build from binary classification with linear regression through polynomial regression, custom scikit-learn transformers, and from-scratch classification metric implementations. Each assignment uses real or synthetic datasets and includes both CodeGrade auto-graded and manually graded submissions.

---

## 📂 File Structure

```
ML-Regression-pipline/
├── README.md
│
├── assignment1.ipynb              ← Johnny Likes Pies: Linear Regression classifier
├── JohnnyPiesData.csv
├── JohnnyPies.png
│
├── assignment2.ipynb              ← California Housing: Multi-source data merging + prep
├── cal_housing_low.csv
├── cal_housing_medium.csv
├── cal_housing_high.csv
├── long_lat.csv
├── ocean_proximity.csv
│
├── assignment3.ipynb              ← Multiple Linear Regression: 3D plotting
├── MultipleLinearRegression.csv
├── LinearDataPlot.png
├── LinearDataPlot_Curve.png
│
├── assignment4.ipynb              ← Custom Transformer + Full Pipeline
├── CustomTransformerData.csv
├── DataTransformation.png
│
├── assignment6.ipynb              ← Classification Metrics from scratch
│
├── assignment7.ipynb              ← Polynomial Regression I (degree 2)
├── PolynomialRegressionData_I.csv
├── PolynomialDataPlot_I.png
├── PolynomialDataPlot_II.png
│
├── assignment8.ipynb              ← Polynomial Regression II (degree 3)
├── PolynomialRegressionData_II.csv
├── PolynomialDataPlot_III.png
└── PolynomialDataPlot_IV.png
```

---

## ⚙️ Requirements

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## 📋 Assignment Summaries

### Assignment 1 — Johnny Likes Pies
**Concept:** Linear regression as a binary classifier using the "Johnny Likes Pies" pattern-recognition dataset.

- One-hot encoding with `pd.get_dummies(drop_first=True)`
- Fitting `sklearn.linear_model.LinearRegression`
- Threshold-based prediction conversion (≥0.5 → 1)
- Accuracy scoring with `sklearn.metrics.accuracy_score`

### Assignment 2 — California Housing Data Manipulation
**Concept:** Merging five separately-delivered CSV files into one clean housing dataset.

- Merging `low/medium/high` price subsets with geographic coordinates
- Outer merging with `ocean_proximity` data
- Dropping rows with missing `medianHouseValue`; filling `housingMedianAge` with median
- Sorting by ID and resetting index

### Assignment 3 — Multiple Linear Regression (3D)
**Concept:** Fitting a multiple linear regression model to 3D data and visualizing the result from four perspectives. *(Manually graded)*

- `scatter3D` with `view_init()` for four subplot angles using `mpl_toolkits.mplot3d`
- `LinearRegression.fit()` on (x, y) → z
- Plotting the regression line of best fit in 3D
- Inferring true model parameters by rounding coefficients to integers (True: `[8, 16]`, intercept: `-9`)

### Assignment 4 — Custom Transformer & Pipeline
**Concept:** Building a custom scikit-learn-compatible transformer and integrating it into a full `ColumnTransformer` pipeline.

- `BaseEstimator` + `TransformerMixin` subclass computing `x1³/x5` as a new feature
- Optional `drop_x4` parameter
- `SimpleImputer` (mean strategy) + `StandardScaler` in a `Pipeline`
- `OneHotEncoder(drop='first')` for categorical column
- `ColumnTransformer` combining numeric pipeline and OHE

### Assignment 6 — Classification Metrics from Scratch
**Concept:** Implementing all major binary classification metrics without using scikit-learn's built-in metric functions.

- `predict(probs, thresh)` — threshold-based class assignment
- `acc_score(labels, preds)` — accuracy
- `error_rate(labels, preds)` — 1 - accuracy
- `prec_recall_score(labels, preds)` — precision and recall via TP/FP/TN/FN counting
- `f_beta(labels, preds, beta)` — generalized F-score
- `TPR_FPR_score(labels, preds)` — TPR and FPR for ROC curve plotting
- All verified against scikit-learn equivalents

### Assignment 7 — Polynomial Regression I (Degree 2)
**Concept:** Fitting a degree-2 polynomial regression to 3D data and inferring true quadratic model parameters. *(Manually graded)*

- `PolynomialFeatures(degree=2, include_bias=False)` transformation
- `LinearRegression` fit on polynomial features
- 3D scatter + curve plotting from four angles
- True model: `z = 8x² + 16y² - 1000` (coefficients: `[8, 0, 0, 0, 16]`, intercept: `-1000`)

### Assignment 8 — Polynomial Regression II (Degree 3)
**Concept:** Extending to a degree-3 polynomial with a cubic response surface. *(Manually graded)*

- `PolynomialFeatures(degree=3, include_bias=False)` — 9 feature terms
- True model: `z = 13x³ + 24y³ - 875` (coefficients: `[13, 0, 0, 0, 0, 0, 0, 0, 24]`, intercept: `-875`)
- Same 4-view 3D visualization approach as assignments 3 and 7

---

## 💡 Key Concepts

- **Linear Regression as Classifier** — applying a 0.5 threshold to regression outputs produces binary classifications; useful for understanding the conceptual bridge to logistic regression
- **Custom Transformers** — subclassing `BaseEstimator` and `TransformerMixin` makes custom preprocessing steps compatible with scikit-learn `Pipeline` and `GridSearchCV`
- **From-Scratch Metrics** — implementing TP/FP/TN/FN counting reinforces understanding of what accuracy, precision, recall, and F-score actually measure
- **Polynomial Feature Expansion** — `PolynomialFeatures` generates interaction and power terms, enabling linear models to fit non-linear surfaces
- **True Model Inference** — rounding fitted coefficients to integers reveals the underlying data-generating equation when noise is small

---

## 📊 Datasets

| File | Assignment | Description |
|------|-----------|-------------|
| `JohnnyPiesData.csv` | 1 | Pie shape/size/shade classification |
| `cal_housing_*.csv`, `long_lat.csv`, `ocean_proximity.csv` | 2 | California housing split across 5 files |
| `MultipleLinearRegression.csv` | 3 | Synthetic (x, y, z) linear data with noise |
| `CustomTransformerData.csv` | 4 | Mixed numeric/categorical data for pipeline testing |
| `PolynomialRegressionData_I.csv` | 7 | Synthetic degree-2 polynomial surface data |
| `PolynomialRegressionData_II.csv` | 8 | Synthetic degree-3 polynomial surface data |

---

## 📝 Notes

- Assignments 3, 7, and 8 are **manually graded** — all code cells must be fully executed before submission
- Assignment 6 explicitly prohibits using built-in scikit-learn metric functions in the custom functions
- Do not round outputs in Assignment 6 — CodeGrade will mark rounded values incorrect

---

## 🔗 References

- [scikit-learn Pipeline Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [scikit-learn PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
- [scikit-learn Custom Transformers](https://scikit-learn.org/stable/modules/preprocessing.html#custom-transformers)
- [Matplotlib 3D Plotting Guide](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html)
