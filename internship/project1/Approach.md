# Cardiac Heart Disease Machine Learning Project — Approach & Historical Documentation

## 1. Project Overview

This project studies a synthetic heart-disease dataset containing 50,000 patient records. The work was developed as an end-to-end machine-learning exercise covering data preparation, exploratory data analysis (EDA), supervised learning, feature engineering, dimensionality reduction, clustering, visualization, and anomaly detection.

The project has two complementary machine-learning goals:

1. **Supervised learning:** predict whether a patient belongs to the `Heart_Disease = 0` or `Heart_Disease = 1` class using the available demographic, lifestyle, medical-history, vital-sign, and laboratory features.
2. **Unsupervised learning:** hide the `Heart_Disease` target and investigate whether patients naturally organize into meaningful groups, what characteristics define those groups, and whether unusual patient profiles can be detected.

The project is notebook-based. It currently does not contain a deployed web application or API.

---

## 2. Problem Statement

Heart disease is influenced by a combination of demographic, lifestyle, and medical risk factors. The purpose of this project is to investigate how these variables interact in a structured machine-learning workflow.

The supervised part asks:

> **Can patient information be used to accurately classify the synthetic `Heart_Disease` target?**

The unsupervised part asks a different question:

> **If the `Heart_Disease` label is not given to the algorithm, do patients naturally form meaningful groups, and what characteristics explain those groups?**

These two questions are intentionally separated. A dataset may contain features that are highly useful for predicting a known target without containing strongly separated natural clusters when that target is removed.

---

## 3. Project Objectives

The project objectives are to:

- validate and understand the raw dataset;
- perform exploratory analysis before modeling;
- build a reproducible supervised-learning workflow;
- compare several classification algorithms using consistent evaluation metrics;
- investigate whether engineered features improve supervised performance;
- prevent preprocessing leakage by using Scikit-learn pipelines;
- apply PCA before distance-based unsupervised methods where appropriate;
- compare centroid-based, density-based, and hierarchical clustering approaches;
- interpret clusters using the original human-readable variables;
- detect unusual observations using Isolation Forest;
- document important implementation decisions, limitations, and changes made during development.

---

## 4. Dataset

The dataset is stored in:

```text
Data/synthetic_heart_disease_dataset.csv
```

It contains:

- **50,000 rows**
- **20 predictor features**
- **1 target column: `Heart_Disease`**

### 4.1 Feature groups

**Demographic features**

- Age
- Gender
- Weight
- Height
- BMI

**Lifestyle features**

- Smoking
- Alcohol_Intake
- Physical_Activity
- Diet
- Stress_Level

**Medical-history / risk-factor features**

- Hypertension
- Diabetes
- Hyperlipidemia
- Family_History
- Previous_Heart_Attack

**Vital-sign / laboratory features**

- Systolic_BP
- Diastolic_BP
- Heart_Rate
- Blood_Sugar_Fasting
- Cholesterol_Total

**Target**

- `Heart_Disease = 0`: no heart disease
- `Heart_Disease = 1`: heart disease

A full description is available in `Data/data_dictionary.md`.

---

## 5. Definition of Done

For this project, the machine-learning analysis is considered complete when the following items are present and reproducible:

- [x] Dataset is loaded and validated.
- [x] Missing values and duplicate rows are checked.
- [x] Valid categorical values are confirmed.
- [x] Target balance is inspected.
- [x] EDA covers numerical, categorical, medical, and target-related patterns.
- [x] Supervised models are trained and compared on a consistent split.
- [x] Cross-validation and test-set metrics are reported.
- [x] Confusion matrices and ROC-AUC are considered in addition to accuracy.
- [x] Feature engineering is tested using a leakage-safe pipeline.
- [x] Unsupervised learning excludes `Heart_Disease` during clustering.
- [x] PCA is used to support dimensionality reduction.
- [x] K-Means, DBSCAN, Agglomerative Clustering, and BIRCH are investigated.
- [x] Cluster meaning is interpreted using original variables.
- [x] t-SNE is used for visualization.
- [x] Isolation Forest is used for anomaly detection.
- [x] Computationally expensive clustering steps are adapted using representative random samples.
- [x] Project limitations are documented.
- [x] Notebook order and project usage are documented.

A deployment is not currently part of this repository. If a later program phase requires a public application, model persistence, Streamlit/FastAPI deployment, or hosted URL, those would be additional deliverables beyond the current notebook-based analysis.

---

# 6. Historical Development of the Project

## 6.1 Stage 1 — Data Preparation

The project began by loading and validating the dataset in `01_data_preparation.ipynb`.

The first checks included:

- dataset shape and column names;
- data types;
- missing values;
- duplicated observations;
- categorical values;
- descriptive statistics;
- target distribution.

An important issue was discovered with the `Alcohol_Intake` feature. The string value `None` represents a real category meaning that the patient does not consume alcohol. Pandas can interpret some text values representing "none" as missing values when reading a CSV.

To preserve the intended category, the data is loaded with behavior that prevents this value from being automatically converted to `NaN`.

After correction, the valid alcohol categories are:

- None
- Low
- Moderate
- High

The dataset contains no actual missing values and no duplicate rows after loading it correctly.

### Target distribution

The target is reasonably balanced:

- `Heart_Disease = 0`: approximately **53.65%**
- `Heart_Disease = 1`: approximately **46.35%**

Therefore, severe class imbalance is not a major issue in the supervised stage.

---

## 6.2 Stage 2 — Exploratory Data Analysis

The next stage, `02_eda.ipynb`, was designed to answer several questions before any model was trained:

1. What does the dataset look like?
2. Is the target balanced?
3. How are numerical measurements distributed?
4. Which patient characteristics differ between target classes?
5. Which categorical and medical conditions show the clearest target relationships?
6. What do correlations suggest?
7. Are there suspicious values or possible outliers?
8. Which variables appear most useful for supervised learning?

The EDA showed that several variables have visibly stronger relationships with the target than others. Important examples include:

- Age
- Cholesterol_Total
- Hypertension
- Diabetes
- Previous_Heart_Attack

Other demographic and lifestyle variables show weaker direct relationships with the target in this synthetic dataset.

This stage provided the basis for selecting and evaluating supervised models rather than immediately fitting algorithms without first understanding the data.

---

# 7. Supervised Learning Approach

## 7.1 Goal

The supervised-learning stage predicts the binary `Heart_Disease` target from the remaining patient features.

The target is removed from the input feature matrix before training.

A consistent train/test split is used so that different models are evaluated on the same unseen observations.

The main evaluation metric used during tuning is **F1-score**, because it balances precision and recall. Additional metrics are reported because a single metric should not determine the final model choice.

The evaluation includes:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Classification report
- Confusion matrix
- False-positive / false-negative analysis
- 5-fold cross-validation

---

## 7.2 Models Evaluated

Three main classifiers were compared in `03_supervised_learning.ipynb`:

### Logistic Regression

Logistic Regression provides a useful linear baseline. Numerical preprocessing is handled using `StandardScaler` inside a pipeline.

The grid search evaluates combinations of regularization strength and penalty type.

### Random Forest

Random Forest provides a nonlinear tree-based model capable of representing interactions and threshold-based relationships between features.

The grid search considers parameters including:

- number of estimators;
- maximum depth;
- minimum samples required to split.

### Decision Tree

A Decision Tree is also evaluated to determine whether a comparatively simple rule-based model can separate the classes.

The grid search varies:

- maximum depth;
- minimum samples required to split.

---

## 7.3 Supervised Results

The main supervised test results are:

| Model | CV F1 | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.919 | 0.9237 | 0.9178 | 0.9176 | 0.9177 | 0.9822 |
| Random Forest | 1.000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Decision Tree | 1.000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

Logistic Regression performs strongly, but the two tree-based models produce perfect scores on the synthetic dataset.

This result initially required extra checking because perfect test performance can indicate target leakage, an invalid split, or overly optimistic evaluation.

---

## 7.4 Investigation of the Perfect Tree-Based Scores

The pipeline and feature construction were checked for common leakage problems:

- `Heart_Disease` is removed from the input features.
- The test set is kept separate from model training.
- Preprocessing is not fitted using the test target.
- Cross-validation is performed on the training data.
- Later preprocessing is moved inside Scikit-learn pipelines.

The perfect performance remains even after these checks.

The important conclusion is therefore not that the model has achieved realistic clinical diagnostic performance. Instead, the synthetic target appears to follow a very strong rule-like relationship that tree models can reconstruct almost exactly from a relatively small subset of features.

### Interpretation

This is a limitation of the synthetic dataset and must be stated clearly:

> **A score of 1.0 on this synthetic target should not be generalized to real medical data or interpreted as evidence of a clinically perfect heart-disease model.**

---

# 8. Feature Engineering and Pipeline Development

The supervised workflow was then extended in `04_feature_engineering_pipeline.ipynb`.

## 8.1 Engineered Features

The following additional variables were created:

- **Pulse Pressure**
- **Mean Arterial Pressure**
- **Age Group**
- **BMI Category**
- **Medical Risk Count**

These features were intended to test whether clinically meaningful transformations or aggregated risk indicators could improve predictive performance.

---

## 8.2 Leakage-Safe Pipeline

A `ColumnTransformer` and Scikit-learn `Pipeline` were introduced so that preprocessing is fitted consistently during cross-validation and model training.

The pipeline handles:

- numerical scaling;
- categorical one-hot encoding;
- model fitting.

This is preferable to fitting preprocessing on the complete dataset before cross-validation, because the pipeline ensures that transformations are learned independently within each training fold.

---

## 8.3 Original vs Engineered Features

Random Forest was compared with and without the engineered variables using 5-fold cross-validation.

Results:

```text
Original features mean CV F1:   1.0000
Engineered features mean CV F1: 1.0000
Improvement:                    0.0000
```

The engineered features therefore did **not** improve Random Forest performance because the original features had already allowed the model to reach the maximum possible score on this synthetic target.

This is still a useful experimental result: feature engineering should be tested rather than automatically assumed to improve a model.

---

## 8.4 Tuned Pipeline Results

The tuned Random Forest selected:

```text
max_depth = 10
min_samples_split = 2
n_estimators = 100
```

with:

```text
Best CV F1 = 1.0000
```

The engineered Logistic Regression pipeline achieved:

```text
Mean CV F1 = 0.9446
CV standard deviation = 0.0010
```

The final test comparison was:

| Model | CV F1 | Accuracy | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest — Original | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Random Forest — Engineered | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Random Forest — Tuned | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Logistic Regression — Engineered | 0.9446 | 0.9441 | 0.9437 | 0.9399 | 0.9882 |

The Random Forest remains the highest-performing supervised model in the project, although its perfect score must be interpreted in the context of the synthetic data-generation process.

---

# 9. Unsupervised Learning Approach

## 9.1 Goal

The unsupervised stage deliberately removes `Heart_Disease` from the feature matrix.

Its goal is **not** to predict heart disease. Instead, it asks whether the predictor variables naturally form meaningful patient groups without being told the correct label.

The objectives are to:

- discover possible patient groups;
- compare different definitions of a cluster;
- identify what characteristics distinguish each group;
- check whether discovered groups happen to differ in heart-disease prevalence afterward;
- visualize the high-dimensional structure;
- identify unusual patient profiles.

The target may be attached back to the final cluster profiles only after clustering for interpretation. It is never supplied to the clustering algorithms.

---

## 9.2 Unsupervised Preprocessing

Categorical variables are first one-hot encoded. The resulting feature matrix is standardized because PCA and the clustering methods used in this project depend strongly on distances and feature scales.

The preprocessing sequence is:

```text
Original predictors
        ↓
One-hot encoding
        ↓
Standardization
        ↓
PCA representations
        ↓
Clustering / visualization
```

---

# 10. PCA — Dimensionality Reduction

After one-hot encoding, the data has a higher-dimensional representation than the original table.

PCA is used because distance-based methods can become less informative or more expensive in high-dimensional spaces.

Different PCA representations serve different purposes:

- approximately **95% retained variance** for K-Means;
- a more compact representation for DBSCAN;
- **2 PCA components** for visualization.

The two-dimensional PCA projection is used only as a visual aid. It should not be treated as containing all information from the complete feature space.

---

# 11. K-Means Clustering

## 11.1 Purpose

K-Means was used as the primary centroid-based clustering method.

Candidate values of `k` were examined using:

- elbow behavior;
- silhouette score;
- cluster interpretability.

A four-cluster solution was retained for interpretation.

---

## 11.2 Cluster Interpretation

Cluster labels have no meaning by themselves, so the generated labels were attached back to the original patient variables.

The cluster profiles revealed an important result: the four groups overlap substantially and do not represent clearly separated cardiovascular-risk populations.

Medical averages such as the following are very similar across the clusters:

- age;
- BMI;
- blood pressure;
- diabetes prevalence;
- hyperlipidemia prevalence;
- cholesterol;
- previous heart attack.

The approximate heart-disease rate is also very similar across the K-Means groups when checked after clustering.

TThe clearest differences between the clusters occur mainly in
lifestyle-related categorical variables, particularly alcohol intake
and diet:

- **Cluster 0:** characterized by moderate alcohol intake.
- **Cluster 1:** characterized strongly by an unhealthy diet, with a
  mixture of alcohol-consumption levels.
- **Cluster 2:** characterized by low alcohol intake and primarily
  average or healthy diets.
- **Cluster 3:** characterized mostly by no alcohol consumption,
  although a smaller subgroup reports high alcohol intake.

Smoking, physical activity, stress level, gender, and most medical
measurements are distributed quite similarly across the four clusters.

The `Heart_Disease` prevalence is also nearly identical across the
clusters, at approximately 46%. Therefore, these clusters should not
be interpreted as low-, medium-, or high-cardiovascular-risk groups.
Instead, K-Means primarily identifies overlapping lifestyle-oriented
profiles.

### Main K-Means conclusion

The K-Means result suggests that the dataset contains weak natural clustering. The groups are driven more by combinations of lifestyle categories than by sharply different levels of cardiovascular disease risk.

This creates an important contrast with the supervised models:

> **Predictive structure and clustering structure are not the same thing.**

The predictors can reconstruct the synthetic target extremely well when the target is known during supervised training, while the same observations do not naturally divide into clearly separated disease-risk clusters when the label is removed.

---

# 12. DBSCAN

## 12.1 Purpose

DBSCAN was added because it defines clusters using local density rather than centroids.

Unlike K-Means:

- the number of clusters does not need to be supplied in advance;
- observations may be assigned the label `-1` and treated as noise;
- results depend strongly on `eps` and `min_samples`.

---

## 12.2 Original Computational Problem

The first DBSCAN optimization approach attempted a comparatively broad hyperparameter search over the full dataset.

This became very slow because every parameter combination requires DBSCAN to perform a new neighborhood search over approximately 50,000 observations.

Using `sample_size` only inside `silhouette_score()` did not solve the main problem because DBSCAN had already been fitted to the complete input before the silhouette calculation occurred.

---

## 12.3 Optimization Decision

The DBSCAN workflow was changed to use a random sample with the same sampling style used elsewhere in the project:

```python
sample_indices = np.random.choice(
    X_pca50.shape[0],
    size=6000,
    replace=False
)

X_dbscan_sample = X_pca50[sample_indices]
```

`replace=False` ensures that the same observation cannot be selected twice.

A k-distance plot is then used to narrow the plausible `eps` range before performing a small parameter search.

The restricted search evaluates combinations such as:

```text
eps:         1.7, 1.8, 1.9, 2.0, 2.1
min_samples: 8, 12, 15, 20
```

DBSCAN evaluation considers three things together:

1. silhouette score;
2. number of non-noise clusters;
3. percentage of observations classified as noise.

A model is not selected merely because it has the highest silhouette score if it achieves that score by discarding an excessive percentage of observations as noise.

---

## 12.4 DBSCAN Interpretation

The DBSCAN investigation supports the conclusion that the feature space does not contain strongly isolated density-based populations.

Changes in the neighborhood parameters can cause DBSCAN either to:

- merge a large portion of the data into very few clusters; or
- classify a substantial number of observations as noise.

This is not considered a failed experiment. DBSCAN tests a fundamentally different assumption from K-Means, and discovering that strong density-separated groups are absent is itself a valid unsupervised-learning result.

---

# 13. Hierarchical Clustering

## 13.1 Agglomerative Clustering

Agglomerative clustering repeatedly merges similar observations into larger groups and can be used to investigate nested cluster structure.

The original idea of performing full Ward-linkage hierarchical clustering on approximately 50,000 observations was computationally expensive and would also produce an unreadable dendrogram.

The workflow was therefore changed to use a representative sample:

```python
sample_indices = np.random.choice(
    X_pca95.shape[0],
    size=2000,
    replace=False
)

X_hier_sample = X_pca95[sample_indices]
```

Several candidate cluster counts are compared using silhouette score, and a truncated dendrogram is used to inspect the high-level hierarchy.

The dendrogram is used as a structural visualization rather than as proof that the dataset contains medically distinct risk categories.

---

## 13.2 BIRCH

BIRCH was included because it provides a more scalable hierarchical-style clustering approach.

Instead of constructing the complete pairwise hierarchy for all observations, BIRCH summarizes the data into a clustering-feature tree.

This makes it suitable for fitting to the complete dataset while Agglomerative Clustering is demonstrated on a representative subset.

Together, these methods allow hierarchical structure to be explored without requiring an impractically expensive full Ward-linkage calculation.

---

# 14. t-SNE Visualization

t-SNE is used as a nonlinear dimensionality-reduction technique for visualization.

Because running t-SNE on all 50,000 observations is expensive and unnecessary for a readable plot, a random sample is used.

The same sampling principle is applied:

```python
sample_indices = np.random.choice(
    X_scaled.shape[0],
    size=5000,
    replace=False
)
```

t-SNE is treated as a visualization tool, not as a formal clustering evaluation metric.

If cluster colors overlap strongly in the t-SNE projection, that visual result is consistent with the low-separation conclusion reached using silhouette scores and cluster profiles.

---

# 15. Isolation Forest Anomaly Detection

Clustering attempts to group observations, while anomaly detection asks a different question:

> **Which individual patient profiles are unusual relative to the rest of the dataset?**

Isolation Forest is therefore used as a complementary unsupervised method.

A contamination assumption of approximately 5% is used, meaning that the algorithm is instructed to identify a small portion of observations as unusual.

The most anomalous observations can then be examined in the original feature space rather than interpreting the anomaly label as a medical diagnosis.

---

# 16. Supervised vs Unsupervised Findings

The most important overall result of the project comes from comparing the two learning settings.

## Supervised finding

When `Heart_Disease` is provided as a known target, tree-based models can reconstruct the synthetic target almost perfectly.

Random Forest and Decision Tree reach:

```text
F1 = 1.000
ROC-AUC = 1.000
```

Logistic Regression also performs strongly but does not perfectly reconstruct the target.

## Unsupervised finding

When `Heart_Disease` is removed, the patient observations do not divide into strongly separated natural disease-risk groups.

K-Means produces overlapping groups whose clearest differences are mainly lifestyle categories. DBSCAN and hierarchical analysis are used to test alternative definitions of cluster structure, but they do not provide evidence of sharply separated patient populations.

## Combined interpretation

This difference demonstrates a fundamental machine-learning concept:

> **A dataset can be highly predictable in supervised learning without being strongly clusterable in unsupervised learning.**

The synthetic heart-disease target appears to follow a learnable decision rule. Supervised algorithms can exploit that rule because they are explicitly shown the correct target during training.

Clustering algorithms receive no such target information. They organize observations only according to geometry, distance, or density in the predictor space. The strongest natural grouping dimensions therefore do not necessarily correspond to the generated heart-disease rule.

---

# 17. Major Challenges and How They Were Resolved

## Challenge 1 — `Alcohol_Intake = None` looked like missing data

**Problem:** Pandas could interpret the intended `None` category as a null value.

**Resolution:** The CSV loading behavior was changed so that `None` remains a valid category.

**Lesson:** Apparent missing values must be checked against the data dictionary and domain meaning before being automatically removed or imputed.

---

## Challenge 2 — Perfect supervised tree scores

**Problem:** Random Forest and Decision Tree produced F1 and ROC-AUC scores of 1.0, raising concern about target leakage.

**Resolution:** Target removal, train/test separation, cross-validation, and pipeline preprocessing were checked. The high score persisted.

**Conclusion:** The synthetic target has a strongly rule-based structure that tree models can reconstruct. The score is documented as a dataset characteristic rather than realistic medical performance.

---

## Challenge 3 — Feature engineering did not improve Random Forest

**Problem:** Engineered features produced no improvement over the original variables.

**Resolution:** The result was retained rather than forcing additional transformations.

**Conclusion:** Feature engineering is an experiment. When the baseline already reaches the performance ceiling, additional features cannot improve the score.

---

## Challenge 4 — DBSCAN hyperparameter optimization was too slow

**Problem:** A broad grid repeatedly fitting DBSCAN to approximately 50,000 observations required excessive computation.

**Resolution:**

- dimensionality was reduced;
- a reproducible random subset was selected with `np.random.choice(..., replace=False)`;
- a k-distance plot was used to narrow the useful `eps` region;
- the grid was reduced to a small plausible range;
- noise ratio was evaluated alongside silhouette score.

**Lesson:** Hyperparameter search strategy should reflect the computational complexity and behavior of the algorithm rather than applying an unnecessarily wide brute-force grid.

---

## Challenge 5 — Silhouette calculation failed for some DBSCAN combinations

**Problem:** Some DBSCAN parameter combinations produced too few valid clusters for silhouette scoring, resulting in errors such as:

```text
ValueError: Number of labels is 1
```

**Resolution:** Noise observations were removed before silhouette evaluation, and silhouette score was calculated only when at least two valid non-noise clusters existed.

**Lesson:** Unsupervised metrics have validity conditions that must be checked before they are calculated.

---

## Challenge 6 — Full hierarchical clustering was impractical

**Problem:** Ward-linkage hierarchical clustering and a dendrogram on all 50,000 observations were computationally expensive and visually unhelpful.

**Resolution:**

- Agglomerative Clustering uses a representative sample;
- the dendrogram is truncated;
- BIRCH is used as the scalable hierarchical-style method for the full dataset.

**Lesson:** Sampling can be a methodological decision rather than merely a shortcut when the complete visualization or pairwise computation would not add practical value.

---

# 18. Reproducibility Decisions

Several choices were made to keep the project reproducible and interpretable:

- `random_state=42` is used where supported.
- NumPy sampling uses a fixed random seed before `np.random.choice`.
- Sampling is performed with `replace=False`.
- The target is explicitly separated from unsupervised inputs.
- Supervised preprocessing is placed inside pipelines.
- The same train/test set is used for fair supervised model comparison.
- Computationally expensive unsupervised methods use documented sample sizes.
- Final cluster interpretation is performed in the original feature space.

---

# 19. Acceptance Criteria Used During Development

A task is considered complete when:

- the relevant notebook cells run without errors;
- the output can be reproduced from the documented notebook order;
- the purpose of the method is explained in Markdown;
- important parameter choices are justified;
- quantitative metrics are reported where appropriate;
- results are interpreted rather than only printed;
- limitations and unexpected outcomes are documented;
- target leakage is avoided;
- expensive methods use a justified, reproducible sampling strategy when necessary;
- changes are committed through the intended Git/GitHub workflow.

---

# 20. Project Structure

```text
project1/
│
├── Data/
│   ├── synthetic_heart_disease_dataset.csv
│   └── data_dictionary.md
│
├── Notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_supervised_learning.ipynb
│   ├── 04_feature_engineering_pipeline.ipynb
│   └── 05_unsupervised_learning.ipynb
│
├── Approach.md
├── README.md
└── requirements.txt
```

---

# 21. Recommended Notebook Execution Order

Run the notebooks in this order:

```text
01_data_preparation.ipynb
        ↓
02_eda.ipynb
        ↓
03_supervised_learning.ipynb
        ↓
04_feature_engineering_pipeline.ipynb
        ↓
05_unsupervised_learning.ipynb
```

The unsupervised notebook is intentionally ordered so that preprocessing and PCA are created before clustering methods use their outputs.

---

# 22. Current Project Status

At the current stage, the analytical machine-learning workflow is complete:

- data preparation completed;
- EDA completed;
- supervised model comparison completed;
- feature engineering and pipeline evaluation completed;
- unsupervised clustering completed;
- dimensionality reduction included;
- anomaly detection included;
- major computational issues addressed;
- technical and historical documentation added.

The repository remains notebook-based and does not currently include deployment.

---

# 23. Limitations

The following limitations are important when interpreting the project:

1. **Synthetic dataset** — The data is generated and should not be treated as clinical evidence.
2. **Perfect tree-based performance** — The synthetic target has a rule-like structure and is much easier to reconstruct than a real medical outcome.
3. **No medical diagnosis** — The project is an educational machine-learning analysis and does not provide medical advice, diagnosis, or treatment recommendations.
4. **Weak natural clusters** — Clustering does not reveal clear low-, medium-, and high-risk patient populations.
5. **Sampling in expensive unsupervised algorithms** — DBSCAN, Agglomerative Clustering, dendrogram visualization, and t-SNE use representative subsets for computational practicality.
6. **Cluster descriptions are descriptive** — Labels such as "moderate alcohol" or "former smoker" summarize dominant patterns and should not be interpreted as causal explanations.
7. **No deployment** — The current repository demonstrates modeling and analysis rather than a production inference service.

---

# 24. Final Conclusion

This project demonstrates a complete comparison between supervised and unsupervised machine-learning approaches on the same heart-disease dataset.

The supervised stage shows that the synthetic `Heart_Disease` target is highly predictable. Logistic Regression performs strongly, while Random Forest and Decision Tree reconstruct the target perfectly. Feature engineering and additional Random Forest tuning do not improve the maximum score, indicating that the original variables already contain enough information for the tree-based decision rule.

The unsupervised stage produces a different result. When the target is removed, the data does not naturally divide into sharply separated cardiovascular-risk groups. K-Means primarily reveals overlapping lifestyle-oriented groups, while DBSCAN and hierarchical methods test whether alternative density or hierarchical structure exists. These results reinforce that high supervised predictability does not imply strong unsupervised clusterability.

The project also demonstrates practical machine-learning decision making. Computationally expensive DBSCAN and hierarchical operations were redesigned using dimensionality reduction, focused parameter ranges, representative random sampling, and scalable alternatives such as BIRCH. Unexpected results, including perfect supervised scores and weak clustering separation, were investigated and documented rather than hidden.

Overall, the project provides an end-to-end example of data validation, exploratory analysis, classification, feature engineering, leakage-safe pipelines, dimensionality reduction, clustering, anomaly detection, model evaluation, result interpretation, and iterative problem solving.
