# Week 5 — Unsupervised Learning

Moves from supervised prediction into unsupervised learning: discovering structure in data without a target — clustering, dimensionality reduction, and anomaly detection.

| Day | Topic | Highlights |
|---|---|---|
| [Day 1](day1/) | K-Means Clustering | Scaled California housing data, used the elbow method and silhouette score to pick k, fit K-Means, visualized clusters geographically, and interpreted 4 district profiles. |
| [Day 2](day2/) | Comparing Clustering Methods | Ran and manually tuned DBSCAN (via `ParameterGrid`), built hierarchical dendrograms, and compared K-Means, DBSCAN, and hierarchical clustering by silhouette score and geography — explaining why DBSCAN scored lower despite arguably finding more realistic clusters. |
| [Day 3](day3/) | Dimensionality Reduction with PCA | Scaled a cardiac dataset, plotted cumulative explained variance, chose 9 components to retain ~96.41% of variance, and visualized component/feature relationships with a heatmap. |
| [Day 4](day4/) | t-SNE & Anomaly Detection | Projected the same cardiac dataset to 2D with t-SNE (colored by DBSCAN/K-Means clusters), compared it to PCA, then ran Isolation Forest to flag and interpret the two most anomalous patients. |

## What this week covers
Week 5 covers the core unsupervised-learning toolkit — clustering algorithms (K-Means, DBSCAN, hierarchical), dimensionality reduction (PCA, t-SNE), and anomaly detection (Isolation Forest) — along with the evaluation tools specific to unsupervised work (elbow method, silhouette score, explained variance) since there's no labeled target to score against directly.
