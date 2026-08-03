# Week 1 - Day 3: NumPy — Numerical Computing

## Goal
Get comfortable with NumPy for array creation, indexing/slicing, and vectorized operations.

## What was done
- Used NumPy to perform basic array operations.
- Practiced creating, indexing, and slicing arrays.
- Practiced reshaping and manipulating arrays.
- Explored vectorized/broadcast operations vs. manual loops.

## Files
- **`jupy_day3.ipynb`** — Single notebook covering:
  - **Array creation:** `np.array`, `np.ones`, `np.zeros`, `np.arange`, `np.random.rand`, `np.linspace`, and `np.reshape`.
  - **Indexing & slicing:** selecting columns, rows, sub-ranges, and boolean-masked selections (e.g. `a[a > 5]`) on a 4x4 array.
  - **Vectorized operations:** element-wise addition/multiplication with broadcasting, matrix multiplication (`@`), scalar multiplication, and `mean()` (overall, per-column, per-row).
  - **Hands-On Lab task:** builds a 4x4 array of values 1–16, prints its shape/dtype, extracts the second column and last row via slicing, and uses a boolean mask to select all values greater than the array's mean.
