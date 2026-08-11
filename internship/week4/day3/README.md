# Week 4 - Day 3: Diagnosing and Fixing Model Fit (Bias/Variance)

## Goal
Deliberately produce overfitting and underfitting, then fix overfitting with regularization — for both a regression and a classification task — and document the evidence.

## What was done (`jupy_day3.ipynb`)
Opened with definitions: bias is error from overly simple assumptions, variance is error from being too sensitive to the training data, and the two trade off against each other — the goal is a model in the middle.

### Part 1 — Regression (California housing, `DecisionTreeRegressor`)
| Configuration | Train R² | Test R² | Diagnosis |
|---|---|---|---|
| Overfit (`max_depth=None`) | 1.000 | 0.622 | High variance |
| Underfit (`max_depth=1`) | 0.316 | 0.279 | High bias |
| Regularized (`max_depth=7`) | 0.716 | 0.651 | Good fit |

The unrestricted tree memorized the training data perfectly but generalized poorly; the depth-1 tree was too simple to capture the pattern at all; capping depth at 7 closed most of the train/test gap while keeping solid test performance.

### Part 2 — Classification (breast cancer, `DecisionTreeClassifier`)
| Configuration | Train Acc. | Test Acc. | Diagnosis |
|---|---|---|---|
| Overfit (`max_depth=None`) | 1.000 | 0.947 | High variance |
| Underfit (`max_depth=1`) | 0.921 | 0.895 | High bias |
| Regularized (`max_depth=3`) | 0.978 | 0.947 | Good fit |

Same pattern: perfect training accuracy with a depth-1 gap to test performance for the overfit tree, both scores low for the underfit tree, and `max_depth=3` producing a much smaller, healthier train/test gap while matching the overfit model's test accuracy.

### Fix applied
In both cases, regularization was done by limiting `max_depth` (reducing model complexity/discouraging reliance on training-set noise), with a note that linear models achieve the same effect via Ridge/Lasso regression.
