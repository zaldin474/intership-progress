# Week 4 - Day 4: Feature Engineering & Hyperparameter Tuning

## Goal
Engineer new features from a raw dataset, tune a Week 3-style model with `GridSearchCV`, and compare the tuned model against the untuned baseline.

## Dataset
`diabetes_prediction_dataset.csv` — patient records (gender, age, hypertension, heart disease, BMI, HbA1c level, blood glucose level, smoking history) with a binary `diabetes` target.

## What was done (`jupy_day4.ipynb`)
- **Cleaning + small EDA:** Checked for missing values and duplicates, dropped duplicates, and looked at value counts for gender/hypertension/heart disease/diabetes plus a diabetes-by-age distribution plot.
- **Step 1 — Feature engineering:** Created two new features and justified each — `BMI_category` (binning BMI into underweight/normal/overweight/obese for easier interpretation) and `critical_blood_sugar` (a flag set to 1 if HbA1c ≥ 6.5 or blood glucose ≥ 126, the standard clinical thresholds).
- **Step 2 — Hyperparameter grid:** Defined a grid over `n_estimators` ([50, 100, 150, 200]) and `max_depth` ([5, 7, 9]) for a `RandomForestClassifier`.
- **Step 3 — GridSearchCV:** Ran `GridSearchCV` with 5-fold cross-validation (F1 scoring), reporting the best parameter combination and its cross-validated score.
- **Step 4 — Tuned vs. untuned:** Compared the tuned model's test-set F1 against an untuned `RandomForestClassifier` baseline — the tuned model performed slightly better, attributed to scikit-learn's default settings already being fairly close to optimal for this dataset's size/complexity.
- **Step 5 — What mattered most:** Extracted feature importances from the tuned model and noted the engineered features didn't rank in the top 5 — explained as an artifact of not dropping the original columns they were derived from, causing scikit-learn to split importance between correlated features. Also grouped CV results by `max_depth` and `n_estimators` to check each hyperparameter's individual effect, finding both landed on the same mean F1 (~0.8009) across the tested range — suggesting neither had a strong effect here. Finished with a bar plot of the top 5 most important features.
