# Week 5 - Day 1: K-Means Clustering

## Goal
Move into unsupervised learning: scale a dataset, use the elbow method and silhouette score to choose k, fit K-Means, and interpret the resulting clusters.

## Dataset
California housing data (`fetch_california_housing`) — used purely for its features (no target), to find natural groupings among districts.

## What was done (`unsupervised_learning_day1.ipynb`)
- **Step 1 — Scaling:** Ran K-Means once on unscaled data to show why it matters, then rebuilt it as a `Pipeline` with `StandardScaler`, since K-Means relies on distance and unscaled large-range features would dominate.
- **Step 2 — Elbow method:** Ran K-Means for k = 1 to 10, plotted inertia against k, and identified two candidate k values (4 and 5) from the elbow.
- **Step 3 — Silhouette score:** Compared silhouette scores for non-scaled data and for the k=3, k=4, and k=5 scaled candidates to pick the best-defined clustering.
- **Step 4 — Visualization:** Since the data has 8 dimensions, plotted the clusters geographically using Longitude/Latitude (with an attached California map image for reference) instead of an abstract scatter plot.
- **Step 5 — Interpretation:** With k=4, described four district profiles — high-income/coastal hubs, an outlier cluster of anomalous districts (extreme room/occupancy values), older established urban districts, and newer inland/suburban developments.
