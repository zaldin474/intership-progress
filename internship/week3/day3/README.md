# Week 3 - Day 3: Building a Classifier

## Goal
Train a classification model, evaluate it with a confusion matrix and classification report, and reason about which metric matters most for the problem.

## Dataset
The breast cancer Wisconsin dataset (`load_breast_cancer`), a binary classification problem (malignant vs. benign), relabeled so `1 = malignant`, `0 = benign`.

## What was done (`jupy_day3.ipynb`)
- **Step 1 — Training:** Split the data into train/test sets, built a pipeline that scales features with `StandardScaler` before fitting a `LogisticRegression` model, and fit it.
- **Step 2 — Predictions & confusion matrix:** Generated predictions and produced the confusion matrix (70 true benign, 1 false positive, 2 false negatives, 41 true malignant).
- **Step 3 — Precision/recall/F1:** Computed a full `classification_report` and interpreted each metric for the malignant class — precision 0.98 (98% of malignant predictions were correct), recall 0.95 (caught ~95% of actual malignant cases), F1 0.96 (a strong balance of the two).
- **Step 4 — Precision vs. recall:** Reasoned that for cancer detection, recall matters more than precision, since a false negative (missing a real malignant case) delays treatment — "never miss a real case."
- **Step 5 — AUC-ROC:** Computed the ROC-AUC score (≈0.9973, indicating excellent separation between the two classes) and plotted the ROC curve.
