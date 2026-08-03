# Week 2 - Day 3: Vectors, Matrices & Dot Products

## Goal
Practice representing data as matrices, computing dot products and matrix multiplication, and understanding shape-mismatch errors.

## What was done (`jupy_day3.ipynb`)
- **Task 1:** Represented three data samples (age, matches, goals/assists) as a 3x3 NumPy matrix.
- **Task 2:** Computed the dot product of one sample vector with a weight vector by hand, then verified it with `np.dot`.
- **Task 3:** Used matrix multiplication (`@`) to produce predictions for all three samples at once.
- **Task 4:** Deliberately triggered a shape-mismatch error by multiplying a (3,3) matrix with a 4-element weight vector, read the resulting `ValueError`, and explained in Markdown why it occurs (the dimensions being summed over don't line up) and how to fix it (match the vector's size to the matrix's inner dimension). Also demonstrated a second, related alignment error between two (2,3) matrices and explained the fix (transpose one matrix so the inner dimensions match).
