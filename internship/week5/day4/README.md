# Week 5 - Day 4: Visualization with t-SNE & Anomaly Detection

## Goal
Reduce the Day 3 dataset to 2D with t-SNE, compare it against the PCA projection, then run Isolation Forest to flag and interpret anomalies.

## Dataset
Same `cardiac arrest dataset-selected-columns.csv` as Day 3.

## What was done (`jupy_day4.ipynb`)
- **Cluster labels for coloring:** Re-derived DBSCAN clusters (tuned via manual grid search from Day 2's approach: `eps=1.0, min_samples=3, metric="euclidean"`, silhouette ≈0.4024) and K-Means clusters (elbow-checked, k=3) to use as coloring for the t-SNE plot.
- **Step 1 — t-SNE:** Ran `TSNE(n_components=2, perplexity=30)` on the scaled data and plotted the 2D projection, colored once by DBSCAN clusters and once by K-Means clusters.
- **Step 2 — t-SNE vs. PCA:** Compared against a 2-component PCA projection (which retains only ~36% of variance in 2D) — concluding PCA is a linear method better suited for understanding broad variance structure with interpretable explained-variance ratios, while t-SNE is nonlinear and better at revealing local neighborhood structure, though its distances/cluster sizes shouldn't be over-interpreted since it's primarily a visualization tool.
- **Step 3 — Isolation Forest:** Ran `IsolationForest(contamination=0.05)` to flag the top 5% most anomalous points, using `decision_function` to rank them, and visualized flagged vs. normal points on the t-SNE projection.
- **Step 4 — Inspecting flagged points:** Examined the two most anomalous points (patient indices 29 and 175) and hypothesized why each was flagged — patient 29 has extremely high cholesterol (327) combined with an oldpeak of 3.4, and patient 175 has very high resting blood pressure (200) combined with an oldpeak of 4.0; both have multiple values far from the mean simultaneously, which is what made them stand out most.
