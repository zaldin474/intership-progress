# Week 4 - Day 1: Train / Validation / Test Splits

## Goal
Build a proper three-way data split, tune a model using only the validation set, and evaluate the final model on the test set exactly once.

## Dataset
The same breast cancer dataset used in Week 3, Day 3.

## What was done (`jupy_day1.ipynb`)
- **Step 1 — 60/20/20 split:** Built a 60/20/20 train/validation/test split with a fixed `random_state`, done as two successive `train_test_split` calls (first splitting off a 20% test set, then splitting the remaining 80% into 75/25 for train/validation).
- **Step 2 — Tuning on validation only:** Trained a scaled `RandomForestClassifier` pipeline on the training set and evaluated it (accuracy and ROC-AUC) against the validation set only.
- **Step 3 — Final test evaluation:** Evaluated the same model on the test set exactly once (accuracy 0.956, ROC-AUC 0.996 — close to the validation numbers of 0.947/0.978), confirming the model generalizes consistently to unseen data.
- **Step 4 — Why not tune on the test set:** Explained in Markdown that tuning against the test set would no longer give an honest, unbiased estimate of performance on genuinely new data.
