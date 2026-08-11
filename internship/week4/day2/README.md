# Week 4 - Day 2: Cross-Validation

## Goal
Evaluate a model with k-fold cross-validation instead of a single train/test split, and understand why stratified folds matter for classification.

## Dataset
Same breast cancer dataset and Random Forest pipeline as [Day 1](../day1/).

## What was done (`jupy_day2.ipynb`)
- **Step 1 — 5-fold CV:** Ran `cross_val_score` with `cv=5` (F1 scoring) on the training set — explicitly noting that CV must be run on the training set only, not the full `X`/`y`, since that would let the model implicitly see test data.
- **Step 2 — Mean & spread:** Reported the mean and spread of the 5 fold scores, and compared them to the single train/test split score (0.965 single-split vs. 0.939 CV mean), concluding the cross-validated estimate is more trustworthy since it averages performance across multiple folds rather than relying on one lucky/unlucky split.
- **Step 3 — Stratified folds:** Explained that scikit-learn automatically uses `StratifiedKFold` when passing an integer `cv` for a classifier, and why that matters — it keeps roughly the same class proportions in every fold as in the full training set. Also built an explicit `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` version to make that behavior visible directly, reporting per-fold scores plus their mean and standard deviation.
