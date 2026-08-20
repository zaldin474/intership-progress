# Week 4 - Day 5: End-to-End Leak-Free Pipeline

## Goal
Build a complete, reproducible classification pipeline for diabetes prediction that keeps preprocessing, tuning, and evaluation strictly free of data leakage, using a single scikit-learn `Pipeline` end to end (unlike Day 4's manual preprocessing).

## Dataset
Same `diabetes_prediction_dataset.csv` as Day 4 (100,000 patient records; 3,854 duplicates removed, leaving 96,146 unique rows), target `diabetes` (0/1).

## What was done (`jupy_day5.ipynb`)
- **Cleaning:** Checked for missing values and duplicates, dropped duplicates.
- **EDA:** Confirmed the target is imbalanced (~8.8% diabetic vs. ~91.2% non-diabetic, motivating F1 over accuracy and a stratified split); found diabetic patients are older on average (~60.9 vs. ~39.9 years), have higher BMI (~32.0 vs. ~26.9), and have substantially higher HbA1c (~6.93 vs. ~5.40) and blood glucose (~194.0 vs. ~132.8) — all used to justify the engineered features carried over from Day 4.
- **Engineered features:** Recreated `BMI_category` and `critical_blood_sugar` from Day 4, and confirmed diabetes rate rises sharply across BMI categories (from <1% underweight to ~18% obese).
- **Stratified split:** Split 80/20 with `stratify=y`, verifying afterward that class proportions matched almost exactly across the full data, train set, and test set.
- **ColumnTransformer + Pipeline:** Built a `ColumnTransformer` applying `StandardScaler` to numeric columns and `OneHotEncoder(handle_unknown="ignore")` to categorical columns, wrapped together with a `RandomForestClassifier` inside one `Pipeline` — ensuring preprocessing is only ever fit on training folds.
- **Baseline CV:** Ran 5-fold cross-validation (F1 scoring) on the untuned pipeline as a baseline.
- **GridSearchCV:** Tuned `n_estimators`, `max_depth`, and `min_samples_split` (referenced via the `model__` prefix since the classifier lives inside the pipeline) with 5-fold CV, and explained step-by-step what happens inside each fold (preprocessing refit each time, only the held-out fold transformed and scored).
- **Baseline vs. tuned:** Compared the untuned pipeline's mean CV F1 against the tuned model's best CV F1, noting the small improvement likely reflects Random Forest's defaults already suiting this dataset well, or that the tested hyperparameter range doesn't strongly affect performance.
