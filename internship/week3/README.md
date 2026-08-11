# Week 3 — Machine Learning with Scikit-Learn

Transition from statistics/EDA into applied machine learning with scikit-learn, starting with the standard model workflow and a first regression model.

| Day | Topic | Highlights |
|---|---|---|
| [Day 1](day1/) | Intro to Scikit-Learn | The 4-step ML workflow (instantiate → fit → predict → score); tried KNN classification and Linear Regression on the Iris dataset; proper 80/20 train/test split on California housing data, with an explanation of why the test set must stay unseen during training. |
| [Day 2](day2/) | Linear Regression | Trained and evaluated a `LinearRegression` model on California housing data (coefficients, MAE, RMSE, R²), compared it against a mean-prediction baseline, and interpreted the results in writing. |
| [Day 3](day3/) | Building a Classifier | Logistic Regression on the breast cancer dataset; confusion matrix, precision/recall/F1, reasoning about which metric matters more, and ROC-AUC. |
| [Day 4](day4/) | Model Comparison | Trained Decision Tree, Random Forest, SVM, and KNN on the same split; compared F1-scores in one table, read Random Forest feature importances, and picked SVM as the best performer with justification. |
| [Day 5](day5/) | End-to-End Mini-Project | Full pipeline on a heart disease risk dataset: EDA, encoding/scaling, five-model comparison (baseline, Logistic Regression, Random Forest, SVM, KNN), and a justified final model selection. |
| [Mini-Project](miniproject/) | Week Checkpoint | A copy of the Day 5 notebook, kept as the week's standalone deliverable. |

## What this week covers
Week 3 is the first machine-learning week: getting comfortable with scikit-learn's API, running a full train/test/evaluate cycle on real regression and classification datasets, comparing multiple model types fairly, and learning to read model metrics (MAE, RMSE, R², precision/recall/F1, ROC-AUC) critically rather than at face value.
