# Week 2 - Day 4: Outlier Detection & Categorical Distributions

## Goal
Visualize numeric variables, detect outliers with the IQR method, and inspect categorical variables for class imbalance.

## Dataset
`StudentsPerformance.csv` — student exam scores plus demographic columns; narrowed down to gender, parental level of education, and the three score columns (math, reading, writing).

## What was done (`jupy_day4.ipynb`)
- **Step 1 — Histograms:** Plotted a histogram for each numeric score (math, reading, writing), each showing a roughly normal distribution slightly skewed right (higher grades clustering around the median).
- **Step 2 — Box plots:** Plotted a box plot per score alongside each histogram to visually spot outliers (small circles below the lower whisker for each subject).
- **Step 3 — IQR outlier flagging:** For each of the three score columns, computed Q1/Q3, the IQR, and the lower/upper whiskers, then flagged rows falling outside that range. Outliers were kept rather than dropped, since they represent real student scores and removing them would compromise the data's integrity.
- **Step 4 — Count plots:** Plotted count plots for the categorical variables (gender, parental level of education) to visualize class balance/imbalance across categories.
