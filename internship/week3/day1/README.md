# Week 3 - Day 1: Intro to Scikit-Learn

## Goal
Learn the standard scikit-learn workflow (instantiate → fit → predict → score) and practice a proper train/test split.

## What was done (`jupy_day1.ipynb`)
- Introduced the 4-step scikit-learn pattern: instantiate the model, fit it to data, predict on new data, and score the result.
- Loaded the classic Iris dataset (`load_iris`) and tried two models on it: `KNeighborsClassifier` (fit and predicted class labels) and `LinearRegression` (fit and predicted, then plotted predictions vs. actual values) — comparing a classification-style model against a regression model on the same data.
- **Hands-On Lab:** Loaded the California housing dataset (`fetch_california_housing`), separated it into features `X` and target `y`, performed an 80/20 train/test split with a fixed `random_state` (via `train_test_split`), and printed the shapes of `X_train`/`X_test`/`y_train`/`y_test` to confirm consistency.
- Explained in Markdown why a model must never see the test set during training (it could memorize the data and appear to perform well while failing to generalize to genuinely new data), identified the housing task as a regression problem (predicting a continuous median house value), and sketched the end-to-end ML workflow from raw dataset through `train_test_split`, `model.fit()`, `model.predict()`, and comparing predictions to the true test values.
