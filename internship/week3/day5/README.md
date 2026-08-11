# Week 3 - Day 5: End-to-End Mini-Project — Heart Disease Risk

## Goal
A full, narrated, end-to-end ML pipeline on a new dataset: decide the task type, do EDA, preprocess properly (fit scalers/encoders on train only), train and compare multiple models against a baseline, and justify the final pick.

## Dataset
`heart_disease_risk_2026.csv` — 9,000 patient records, 27 columns (demographics, cholesterol, blood pressure, sleep, exercise-induced angina, etc.), target: `has_heart_disease` (binary classification, no missing values or duplicates).

## What was done (`jupy_day5.ipynb`)
### EDA
- Checked class balance (~percentage of patients with heart disease) and its relationship to age via count/histogram plots.
- Compared LDL ("bad") vs. HDL ("good") cholesterol distributions by disease status — found a positive correlation between high LDL and disease, negative for high HDL.
- Binned sleep hours into intervals and plotted heart-disease rate per interval against the overall prevalence as a reference line.
- Built a correlation heatmap (masked to the lower triangle) across all numeric features and called out the strongest relationships: fasting blood sugar vs. HbA1c (0.88), total cholesterol vs. LDL (0.84), systolic vs. diastolic blood pressure (0.77), age vs. max heart rate (−0.73), and exercise-induced angina vs. heart disease (0.45). Also ranked every feature's individual correlation with the target, and noted a full pair plot was too cluttered to be useful here.

### Modeling
- One-hot encoded categorical columns (`pd.get_dummies`, dropping the first category), split into train/test.
- Trained five scaled pipelines: a `DummyClassifier` baseline (most-frequent strategy), `LogisticRegression`, `RandomForestClassifier`, `SVC`, and `KNeighborsClassifier`.
- Evaluated all five on accuracy, ROC-AUC, confusion matrix, and classification report, then assembled the results into one comparison table:

| Model | Accuracy | ROC-AUC | Weighted F1 |
|---|---|---|---|
| Baseline | 0.6941 | 0.5000 | 0.57 |
| Logistic Regression | **0.9022** | **0.9579** | **0.90** |
| Random Forest | 0.8826 | 0.9417 | 0.88 |
| SVM | 0.8919 | 0.9489 | 0.89 |
| KNN | 0.8181 | 0.8530 | 0.81 |

### Selected model & justification
**Logistic Regression** was chosen: highest accuracy (90.22%) and ROC-AUC (0.9579), an F1-score of 0.93 for the disease class and 0.83 for the no-disease class, and the fewest total misclassifications (264, vs. 292 for SVM, 317 for Random Forest, 491 for KNN). The baseline was ruled out for having a ROC-AUC of only 0.50 (no real discriminative power) despite its 69% accuracy, illustrating why accuracy alone is misleading on this imbalanced dataset.
