# Week 4 — Model Validation & Generalization

Focused on doing evaluation correctly: proper data splitting, cross-validation, and diagnosing/fixing overfitting vs. underfitting.

| Day | Topic | Highlights |
|---|---|---|
| [Day 1](day1/) | Train/Validation/Test Splits | 60/20/20 split on the breast cancer dataset; tuned only against validation, then evaluated on the held-out test set exactly once; explained why tuning on the test set would be dishonest. |
| [Day 2](day2/) | Cross-Validation | 5-fold `cross_val_score` on the same model; compared the CV mean to the single-split score; confirmed and explained stratified folds for classification. |
| [Day 3](day3/) | Diagnosing & Fixing Model Fit | Deliberately overfit and underfit a decision tree (regression and classification), then used `max_depth` regularization to shrink the train/test gap, with full score tables and diagnosis for each case. |

## What this week covers
Week 4 shifts from "can I train a model" to "can I trust my evaluation of it" — covering the mechanics of validation splits, cross-validation, and the bias/variance tradeoff that explains why models over- or under-perform, and how to fix it.
