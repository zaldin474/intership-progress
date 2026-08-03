# Week 3 - Day 2: Linear Regression

## Goal
Train a Linear Regression model, interpret its coefficients, evaluate it with standard regression metrics, and compare it against a naive baseline.

## What was done (`jupy_day2.ipynb`)
Using the California housing dataset (`fetch_california_housing`) with an 80/20 train/test split (`random_state=42`):
- **Task 1 — Training:** Fit a `LinearRegression` model on the training set and generated predictions on the test set.
- **Task 2 — Coefficients:** Printed the model's coefficients and intercept per feature, noting that raw coefficient sizes aren't directly comparable across features because the features are on different scales (the largest raw coefficient belonged to `AveBedrms`).
- **Task 3 — Evaluation:** Computed R² (via `model.score`), MAE, MSE, and RMSE on the test set (MAE ≈ 0.533, RMSE ≈ 0.746, R² ≈ 0.576 — target is in units of $100,000), with a written explanation of what each metric represents (MAE = average prediction error; RMSE = error that penalizes large mistakes more; R² = share of variance explained).
- **Task 4 — Baseline comparison:** Built a baseline that always predicts the training-set mean, computed its RMSE, and compared it to the model's RMSE — the Linear Regression model's lower RMSE shows it adds real predictive value over always guessing the average.
- **Task 5 — Interpretation:** Documented that the model explains ~57.6% of the variance in house values, is useful but not highly accurate (42.4% unexplained), and that the remaining error may reflect nonlinear relationships in the housing data not captured by a linear model. Finished with a scatter plot of actual vs. predicted values.
