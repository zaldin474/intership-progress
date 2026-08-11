# Week 3 - Day 4: Model Comparison

## Goal
Train several different classifier types on the same data and compare them fairly on the same metric, then pick a winner and explain why.

## Dataset
Same breast cancer dataset and train/test split as [Day 3](../day3/).

## What was done (`jupy_day4.ipynb`)
- **Step 1 — Training four models:** Built scaled pipelines for a `DecisionTreeClassifier`, `RandomForestClassifier`, `SVC` (SVM), and `KNeighborsClassifier`, all trained on the same split.
- **Step 2 — Common-metric comparison:** Generated a `classification_report` for each model and assembled malignant-class F1-score/recall into one comparison table: Decision Tree 0.91/0.91, Random Forest 0.94/0.93, SVM 0.98/0.95, KNN 0.93/0.93.
- **Step 3 — Feature importances:** Pulled the Random Forest's `feature_importances_` (extracting the classifier step out of the pipeline first, after hitting and explaining an `AttributeError` from calling it on the pipeline directly) and interpreted the scores as showing which features the model relies on most heavily.
- **Step 4 — Best model:** Identified **SVM** as the best performer on both F1 and recall, and explained why: its ability to find an optimal separating hyperplane (with kernels for non-linear cases) and its lower tendency to overfit compared to Decision Trees and KNN, which matters since both F1 and recall are important in this medical context.
