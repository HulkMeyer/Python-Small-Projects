# Picture Phrase — NumPy Array Transformation Assignment

> A creative NumPy puzzle: reverse-engineer a sequence of array transformations applied to an image's RGB values to reconstruct the original hidden phrase.

![Category](https://img.shields.io/badge/Category-Data%20Analysis-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Libraries](https://img.shields.io/badge/Libraries-numpy%20%7C%20matplotlib-orange)
![Course](https://img.shields.io/badge/Course-DTSC%20580-lightgrey)

---

## 📌 Overview

An image containing a hidden phrase was converted into a NumPy array of RGB values, then transformed through a specific sequence of mathematical operations. This assignment reverses those transformations step-by-step — dtype conversion, scalar arithmetic, linspace-based subtraction, element updates, and selective index addition — ultimately reconstructing the original image and revealing the phrase.

---

## 📂 File Structure

```
data-analysis/picture-phrase-numpy/
├── README.md
├── picture_phrase.ipynb
└── array.txt
```

---

## ⚙️ Requirements

```bash
pip install numpy matplotlib
```

---

## 🚀 How to Run

```bash
cd data-analysis/picture-phrase-numpy
jupyter notebook picture_phrase.ipynb
```

`array.txt` must be in the same directory as the notebook.

---

## 📋 Topics Covered

- **Loading Arrays from Text** — `np.loadtxt()` with `dtype='U32'` for string-typed numeric data
- **dtype Conversion** — `astype('float64')` to enable mathematical operations
- **Scalar Array Arithmetic** — multiplying, adding, and subtracting constants from entire arrays
- **`np.sum()` on a Sub-Array** — summing a small array and adding the result to a large array
- **`np.linspace()`** — generating evenly spaced values for position-wise subtraction
- **Array Copying** — `.copy()` to avoid creating views that would modify the original
- **Element-wise Index Update** — directly assigning to a specific index position
- **Selective Range Addition** — adding values to slices defined by index ranges (simulating range operations without explicit loops)
- **Image Display** — using `matplotlib.pyplot` to render the final RGB array as an image

---

## 💡 Key Concepts

- **Views vs. Copies** — NumPy array slices are views by default; `.copy()` is essential when you need an independent array
- **`linspace` for position-based operations** — `np.linspace(1, n, n)` creates a positional array for subtracting 1 from element 1, 2 from element 2, etc., without any loop
- **RGB Arrays** — images are stored as 3D arrays (height × width × 3 channels); this assignment works with a flattened 1D version

---

## 📝 Notes

- This is a **CodeGrade assignment** — each step is saved as a numbered variable (`Q1`, `Q2`, etc.) for auto-grading
- The code check for `Q5` should produce: `array([ 340., 50176., 353., ..., 46225., 474., 124609.])`
- The loop used for `Q7` is functional but not optimal — `np.where` or slice assignment would be more Pythonic

---

## 🔗 References

- [NumPy `linspace` Documentation](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [NumPy `loadtxt` Documentation](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html)
