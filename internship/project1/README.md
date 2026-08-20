# Cardiac Heart Disease Machine Learning Project

## Project Overview

This project applies machine-learning methods to a synthetic heart-disease dataset.

The main goal is to explore the data, prepare it for modeling, compare supervised classification models, and test whether feature engineering improves the results.

The project is notebook based and does not include a web application or API.

For the detailed project approach, supervised/unsupervised methodology, development history, decisions, challenges, and conclusions, see [`Approach.md`](Approach.md).

## Dataset

The dataset contains 50,000 rows and 21 original columns.

The target variable is:

- `Heart_Disease`
  - `0` = No heart disease
  - `1` = Heart disease

The dataset includes patient information such as age, BMI, blood pressure, cholesterol, diabetes, hypertension, previous heart attack, and lifestyle-related features.

`Alcohol_Intake = None` is treated as a valid category meaning that the patient does not consume alcohol. It is not treated as a missing value.

## Project Structure

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
│   └── 04_feature_engineering_pipeline.ipynb
│
├── outputs/
│   ├── confusion_matrix/
│   ├── figures/
│   └── results/
│
├── README.md
├── Approach.md
└── requirements.txt
```

## Notebook Order

### 01 - Data Preparation

The first notebook loads and checks the dataset.

It covers:

- dataset shape and columns
- data types
- missing values
- duplicate rows
- categorical values
- invalid or unusual values
- target definition

### 02 - Exploratory Data Analysis

The EDA notebook studies the main patterns in the dataset.

It includes:

- descriptive statistics
- target class balance
- numerical distributions
- categorical distributions
- feature vs target relationships
- binary medical-condition comparisons
- lifestyle-feature comparisons
- correlation matrix
- potential outlier checks

Some of the clearest direct relationships with `Heart_Disease` are found in:

- Age
- Cholesterol_Total
- Hypertension
- Diabetes
- Previous_Heart_Attack

Several other features show much weaker direct relationships in this synthetic dataset.

### 03 - Supervised Learning

The supervised-learning notebook compares classification models using the same train/test split and evaluation approach.

Models include:

- Logistic Regression
- Random Forest
- Decision Tree

Evaluation includes:

- 5-fold cross-validation
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Classification report
- Confusion matrix
- False-positive and false-negative comparison
- ROC curves

### 04 - Feature Engineering and Pipeline

The final supervised notebook creates extra features and uses Scikit-learn pipelines for repeatable preprocessing and training.

Engineered features include:

- Pulse Pressure
- Mean Arterial Pressure
- Age Group
- BMI Category
- Medical Risk Count

The notebook compares:

- Random Forest with original features
- Random Forest with engineered features
- Tuned Random Forest
- Logistic Regression with engineered features

The preprocessing is performed inside `ColumnTransformer` and `Pipeline`, so scaling and one-hot encoding are fitted only on the training data during cross-validation.


### 05 - Unsupervised Learning

The unsupervised-learning notebook removes `Heart_Disease` from the clustering inputs and investigates whether patient records naturally form meaningful groups.

It includes:

- PCA dimensionality reduction
- K-Means clustering and cluster profiling
- DBSCAN with sampled hyperparameter exploration
- sampled Agglomerative Clustering and dendrogram analysis
- BIRCH on the full dataset
- t-SNE visualization
- Isolation Forest anomaly detection
- comparison of supervised predictability with unsupervised clusterability

The main finding is that natural clusters overlap substantially and are driven more by lifestyle-category patterns than by clearly separated heart-disease risk groups.

## Note About the Perfect Tree-Based Scores

Random Forest and Decision Tree models can reach an F1 score of 1.0 on this dataset.

The pipeline was checked for target leakage:

- `Heart_Disease` is removed from the feature matrix.
- The train/test split is made before fitted preprocessing.
- Scaling and one-hot encoding are fitted inside the pipeline.
- Cross-validation is performed only on the training set.

Even after these checks, a shallow Decision Tree can separate the target perfectly.

This suggests that the synthetic target is strongly rule-based and can be reconstructed from a small group of features. Therefore, the perfect score should not be interpreted as realistic clinical performance.

## How to Run

1. Open the project folder.
2. Make sure the required Python packages are installed.
3. Start Jupyter Notebook or JupyterLab.
4. Open the `Notebooks/` folder.
5. Run the notebooks in this order:

```text
01_data_preparation.ipynb
02_eda.ipynb
03_supervised_learning.ipynb
04_feature_engineering_pipeline.ipynb
05_unsupervised_learning.ipynb
```

The notebooks use a relative path to the dataset:

```text
../Data/synthetic_heart_disease_dataset.csv
```

## Requirements

Main packages used:

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter

Install the requirements with:

```bash
pip install -r requirements.txt
```

## Limitations

- The dataset is synthetic and should not be treated as real clinical evidence.
- The project predicts a dataset target only; it does not provide medical diagnosis or treatment recommendations.
- Very high model performance is partly caused by the strong rule-like structure of the synthetic target.
- Relationships found in this dataset should not automatically be generalized to real patients.
