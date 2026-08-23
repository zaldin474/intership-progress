# Phase 3 Capstone — Sprint 1 Plan & Backlog

## Project
**Heart Disease Prediction**

## Phase
Phase 3 — Sprint 1

## Week
Week 6 — Deep Learning Introduction

---

## 1. Problem Statement

The goal of this project is to build a machine learning system that predicts whether a person has heart disease based on demographic, lifestyle, and clinical features.

The target variable is:

`Heart Disease Status`

This is a **binary classification** problem:

- `No` = No heart disease
- `Yes` = Heart disease

The project will first establish a classical machine learning baseline, then build and evaluate a neural network and compare its performance against that baseline.

---

## 2. Dataset Summary

The provided dataset contains:

- **Rows:** 10,000
- **Columns:** 21
- **Target:** `Heart Disease Status`
- **No:** 8,000 (80.0%)
- **Yes:** 2,000 (20.0%)
- **Duplicate rows:** 0

The target is moderately imbalanced, so model evaluation should not rely on accuracy alone. Precision, recall, F1-score, ROC-AUC, and the confusion matrix should also be considered.

### Missing Values

The dataset contains missing values in some features. These must be handled as part of preprocessing without leaking information from the test set.

Main missing-value counts:

- `Alcohol Consumption`: 2,586
- `Cholesterol Level`: 30
- `Diabetes`: 30
- `Sugar Consumption`: 30
- `Age`: 29
- `CRP Level`: 26
- `Triglyceride Level`: 26
- `High Blood Pressure`: 26
- `High LDL Cholesterol`: 26
- `Low HDL Cholesterol`: 25
- `Sleep Hours`: 25
- `Exercise Habits`: 25
- `Smoking`: 25
- `Stress Level`: 22
- `Fasting Blood Sugar`: 22
- `BMI`: 22
- `Family Heart Disease`: 21
- `Homocysteine Level`: 20
- `Blood Pressure`: 19
- `Gender`: 19

---

## 3. Definition of Done

The capstone project is considered complete when it includes:

- A clean and documented Jupyter Notebook covering the full ML pipeline:
  - Exploratory Data Analysis
  - Data cleaning and preprocessing
  - Feature preparation
  - Baseline modelling
  - Neural network modelling
  - Model evaluation and comparison
- A trained model with clearly reported evaluation metrics.
- A working deployment through Streamlit or FastAPI.
- A GitHub repository containing:
  - Clean README
  - `requirements.txt`
  - Model artifacts
  - Organized project files
- A short technical write-up explaining the problem, methodology, experiments, results, and conclusions.
- Work completed through feature branches and reviewed pull requests.

---

## 4. Sprint 1 Goal

**Understand and prepare the heart disease dataset, establish a reproducible classical machine learning baseline, and build the first neural network model that can be evaluated against that baseline.**

The baseline model must be completed before the neural network so that every later model has a meaningful score to beat.

---

## 5. Sprint 1 Backlog

| ID | Task | Estimated Effort | Priority | Status |
|---|---|---:|---|---|
| S1-01 | Set up GitHub repository and project structure | 1 hr | High | To Do |
| S1-02 | Finalize and document the heart disease dataset | 1 hr | High | To Do |
| S1-03 | Inspect dataset structure and data types | 1 hr | High | To Do |
| S1-04 | Check missing values, duplicates, and data quality issues | 1 hr | High | To Do |
| S1-05 | Perform exploratory data analysis | 3 hrs | High | To Do |
| S1-06 | Prepare features and target variable | 2 hrs | High | To Do |
| S1-07 | Encode categorical variables, impute missing values, and scale numerical features | 2 hrs | High | To Do |
| S1-08 | Create train/validation/test split | 1 hr | High | To Do |
| S1-09 | Train Logistic Regression baseline | 2 hrs | High | To Do |
| S1-10 | Evaluate and record baseline metrics | 1 hr | High | To Do |
| S1-11 | Plot and study ReLU, sigmoid, and tanh activation functions | 2 hrs | Medium | To Do |
| S1-12 | Select and justify output activation and loss function | 1 hr | High | To Do |
| S1-13 | Perform a small forward-pass experiment | 2 hrs | Medium | To Do |
| S1-14 | Document the neural-network training loop | 1 hr | Medium | To Do |
| S1-15 | Run learning-rate experiments and compare loss curves | 2 hrs | Medium | To Do |
| S1-16 | Open mid-sprint pull request for mentor review | 1 hr | High | To Do |
| S1-17 | Build the first TensorFlow/Keras neural network | 3 hrs | High | To Do |
| S1-18 | Train and evaluate the neural network | 2 hrs | High | To Do |
| S1-19 | Plot training and validation loss/accuracy curves | 1 hr | High | To Do |
| S1-20 | Add dropout and/or batch normalization | 2 hrs | Medium | To Do |
| S1-21 | Tune selected neural-network hyperparameters | 2 hrs | Medium | To Do |
| S1-22 | Add EarlyStopping and preserve the best weights | 1 hr | Medium | To Do |
| S1-23 | Compare baseline and neural-network metrics | 1 hr | High | To Do |
| S1-24 | Prepare Sprint Review evidence | 1 hr | High | To Do |
| S1-25 | Complete Sprint Retrospective | 1 hr | High | To Do |

---

## 6. Day 1 Backlog — Dataset, EDA & Baseline

### S1-01 — Repository Setup

**Task**

Create the GitHub repository and initial project structure.

**Acceptance Criteria**

- Repository exists and is accessible.
- Project folders are organized clearly.
- `README.md` exists.
- `requirements.txt` exists or has an initial placeholder.
- `.gitignore` is configured.
- Work is performed on a feature branch rather than directly on `main`.
- Changes are committed with a descriptive commit message.

---

### S1-02 — Dataset Finalization

**Task**

Use and document the provided heart disease dataset.

**Acceptance Criteria**

- Dataset source/file is documented.
- Dataset loads successfully in Pandas.
- Dataset dimensions are recorded as **10,000 rows × 21 columns**.
- Target variable is identified as `Heart Disease Status`.
- Target class distribution is documented.
- Dataset purpose is explained in Markdown.
- Notebook cells run without errors.

---

### S1-03 / S1-04 — Initial Data Inspection

**Task**

Understand the structure and quality of the dataset.

**Acceptance Criteria**

The notebook includes:

- `df.head()`
- Dataset shape
- `df.info()`
- Summary statistics
- Missing-value inspection
- Duplicate-row inspection
- Identification of numerical and categorical variables
- Target distribution
- Markdown observations describing important findings

The inspection should explicitly note:

- The target distribution is approximately **80% No / 20% Yes**.
- The dataset contains missing values that require preprocessing.
- Duplicate rows should be checked and documented.

---

### S1-05 — Exploratory Data Analysis

**Task**

Explore important relationships between the available features and `Heart Disease Status`.

**Suggested Features to Inspect**

Examples include:

- Age
- Blood Pressure
- Cholesterol Level
- BMI
- Smoking
- Diabetes
- Exercise Habits
- Triglyceride Level
- Fasting Blood Sugar
- CRP Level
- Other demographic, lifestyle, or clinical variables present in the dataset

**Acceptance Criteria**

- Target class distribution is visualized.
- Important numerical features are explored.
- Important categorical features are compared with heart disease status.
- Relevant distributions and relationships are visualized.
- Findings are explained in Markdown.
- Visualizations have appropriate titles and labels.
- Notebook runs without errors.

---

### S1-06 / S1-07 — Data Preparation

**Task**

Prepare the dataset for machine learning.

**Acceptance Criteria**

- Features `X` and target `y` are separated correctly.
- Target values are encoded consistently, for example:
  - `No -> 0`
  - `Yes -> 1`
- Missing values are handled appropriately.
- Categorical features are encoded.
- Numerical features have appropriate data types.
- Scaling is applied where appropriate.
- Preprocessing is fitted only on training data.
- A reproducible preprocessing pipeline is preferred.
- All preprocessing decisions are documented.

---

### S1-08 — Dataset Split

**Task**

Create training, validation, and/or test datasets.

**Acceptance Criteria**

- Features `X` and target `y` are separated correctly.
- Data is split reproducibly using a fixed `random_state`.
- Stratification is used to preserve the approximately 80/20 target distribution.
- Training and test data remain separate.
- Any validation data is created only from the training portion.

---

### S1-09 — Baseline Model

**Task**

Train a simple classical machine learning baseline before using a neural network.

**Selected Baseline**

**Logistic Regression**

**Acceptance Criteria**

- Logistic Regression trains without errors.
- Model is evaluated on unseen data.
- Preprocessing and model are reproducible.
- Model configuration is documented.
- No neural network is used as the baseline.
- Baseline results are recorded clearly.

---

### S1-10 — Baseline Evaluation

**Task**

Record the score that later models must beat.

**Metrics**

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix

**Acceptance Criteria**

- All selected metrics are calculated.
- Results are documented in Markdown.
- Class imbalance is considered when interpreting accuracy.
- Performance on the positive `Yes` class is discussed.
- Baseline metric values are clearly recorded.
- A statement identifies the baseline score that the neural network must compete with.

Example:

> The Logistic Regression model is the Sprint 1 baseline. Future neural-network models will be compared against its performance, with particular attention to recall, F1-score, and ROC-AUC because the positive heart-disease class is less common.

---

## 7. Day 2 Backlog — Activations, Forward Propagation & Loss

### Tasks

- Plot ReLU, sigmoid, and tanh.
- Explain why nonlinear activations are necessary.
- Choose the correct output activation for Heart Disease Prediction.
- Choose the appropriate loss function.
- Perform a simple forward-pass calculation.

### Planned Model Choice

Because Heart Disease Prediction is binary classification:

- Hidden activation: **ReLU**
- Output activation: **Sigmoid**
- Loss function: **Binary Cross-Entropy**

### Acceptance Criteria

- Activation plots run without errors.
- Each activation is briefly explained.
- Output activation choice is justified.
- Loss-function choice is justified.
- Forward-pass result is documented in Markdown.

---

## 8. Day 3 Backlog — Training Mechanics & Mentor Review

### Tasks

- Explain the four-step training loop:
  1. Forward pass
  2. Compute loss
  3. Backpropagation
  4. Update weights
- Explain gradient descent.
- Explain learning rate.
- Run experiments with different learning rates.
- Plot loss curves.
- Explain backpropagation conceptually.
- Open a pull request for mentor review.

### Acceptance Criteria

- Training loop is explained clearly.
- At least three learning-rate behaviors are tested or demonstrated:
  - Too low
  - Reasonable
  - Too high
- Loss curves are plotted.
- Results are discussed.
- Pull request contains the current Sprint 1 notebook/work.
- Mentor feedback is addressed before merge.

---

## 9. Day 4 Backlog — Keras Neural Network

### Tasks

- Build a TensorFlow/Keras Sequential model.
- Compile the model.
- Train using validation data.
- Evaluate on test data.
- Plot training history.
- Add dropout and/or batch normalization.
- Compare results with the initial neural network.

### Initial Architecture

A reasonable starting architecture is:

```python
Dense(64, activation="relu")
Dense(32, activation="relu")
Dense(1, activation="sigmoid")
```

The architecture may be adjusted after preprocessing determines the final input feature count.

### Acceptance Criteria

- Network architecture matches the binary classification task.
- Model compiles successfully.
- Adam optimizer is used initially.
- Binary cross-entropy is used.
- Model trains for at least 30 epochs unless EarlyStopping is introduced.
- Training and validation curves are plotted.
- Overfitting or underfitting is diagnosed.
- Test metrics are compared with the Logistic Regression baseline.

---

## 10. Day 5 Backlog — Tuning, Evaluation & Sprint Review

### Tasks

- Tune one hyperparameter at a time.
- Experiment with learning rate, network size, dropout, or batch size.
- Add EarlyStopping.
- Keep the best model weights.
- Create a final metric comparison table.
- Prepare Sprint Review.
- Complete Sprint Retrospective.

### Acceptance Criteria

- Experiments are recorded clearly.
- Only one major variable is changed at a time where possible.
- Validation performance is compared across experiments.
- EarlyStopping is implemented.
- Best model is evaluated on the test set.
- Baseline and neural network are compared directly.
- All Sprint 1 work is committed.
- Pull request is reviewed and merged.
- Sprint Retrospective is completed.

---

## 11. Baseline Comparison Table

Complete this during Sprint 1.

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression Baseline | TBD | TBD | TBD | TBD | TBD |
| Initial Neural Network | TBD | TBD | TBD | TBD | TBD |
| Tuned Neural Network | TBD | TBD | TBD | TBD | TBD |

---

## 12. Git Branch & Pull Request Workflow

### Main Branch

```text
main
```

### Sprint 1 Feature Branch

```text
feature/sprint1-baseline
```

Additional branches may be created for later work if useful:

```text
feature/sprint1-neural-network
feature/sprint1-tuning
```

### Workflow

1. Pull the latest `main`.
2. Create or switch to the appropriate feature branch.
3. Complete a focused set of changes.
4. Run notebook/code and verify it works.
5. Commit using a descriptive message.
6. Push the feature branch.
7. Open a pull request.
8. Request mentor review.
9. Address review comments.
10. Merge only after approval.

### Example Commit Messages

```text
Add heart disease dataset inspection and EDA
Add preprocessing pipeline for heart disease data
Add logistic regression baseline model
Document baseline evaluation metrics
Add neural network activation experiments
Add Keras neural network training pipeline
Add dropout and training history analysis
Add Sprint 1 tuning results
Complete Sprint 1 retrospective
```

---

## 13. Daily Stand-Up Template

### Yesterday / Completed

- What did I complete?

### Today / Next

- What will I work on next?

### Blockers

- Are there any dataset, code, modelling, environment, or Git issues blocking progress?

---

## 14. Sprint Review Evidence

Before the Sprint Review, prepare:

- Sprint goal
- Completed backlog tasks
- Dataset overview
- Important EDA findings
- Missing-value handling strategy
- Baseline model and metrics
- Neural-network architecture
- Training and validation loss curves
- Neural-network metrics
- Baseline vs neural-network comparison
- Tuning experiments
- Best model result
- Remaining/incomplete tasks with reasons

---

## 15. Sprint Retrospective

### What Went Well

- TBD

### What Could Be Improved

- TBD

### One Concrete Action for Sprint 2

- TBD

---

## 16. Sprint 1 Completion Checklist

- [ ] Sprint goal confirmed
- [ ] Sprint backlog documented
- [ ] Heart disease dataset finalized
- [ ] Dataset structure documented
- [ ] Missing values investigated
- [ ] EDA completed
- [ ] Data preprocessing completed
- [ ] Logistic Regression baseline trained
- [ ] Baseline metrics recorded
- [ ] Activation functions studied
- [ ] Output activation justified
- [ ] Loss function justified
- [ ] Forward-pass experiment completed
- [ ] Training loop explained
- [ ] Learning-rate experiments completed
- [ ] Mid-sprint pull request opened
- [ ] Mentor feedback addressed
- [ ] Keras neural network built
- [ ] Neural network trained
- [ ] Training/validation curves plotted
- [ ] Dropout and/or batch normalization tested
- [ ] Hyperparameter tuning completed
- [ ] EarlyStopping added
- [ ] Baseline and neural-network metrics compared
- [ ] Sprint Review prepared
- [ ] Sprint Retrospective written
- [ ] Sprint 1 pull request approved and merged

---

## Sprint 1 Baseline to Beat

**Model:** Logistic Regression

**Primary comparison metrics:** Recall, F1-score, and ROC-AUC

**Baseline score:** TBD after Day 1 training

All later neural-network results must be compared against this baseline.
