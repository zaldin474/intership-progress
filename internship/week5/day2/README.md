# Week 5 - Day 2: Comparing Clustering Methods

## Goal
Run DBSCAN and hierarchical clustering on the same data as Day 1, tune DBSCAN, and compare all three clustering methods (K-Means, DBSCAN, hierarchical) on the same dataset.

## Dataset
California housing Latitude/Longitude coordinates (`fetch_california_housing`).

## What was done (`jupy_day2.ipynb`)
- **Step 1 — DBSCAN:** Ran an initial DBSCAN (`eps=0.2, min_samples=15`) on the raw lat/long data, checked resulting cluster/noise counts and silhouette score, and found the results unsatisfying.
- **DBSCAN optimization:** Since `GridSearchCV` doesn't apply to unsupervised models, wrote a manual grid search over `eps` and `min_samples` using `ParameterGrid` on scaled data, improving the silhouette score from 0.1103 (default) to 0.3675 (tuned).
- **Step 2 — Hierarchical dendrogram:** Built a dendrogram on a 1,000-row sample (full data being too large to visualize), choosing a cut height of 5 to yield 7 clusters, and also built one on the full dataset (cut height 30 → 6 clusters) for comparison.
- **Step 3 — Three-way comparison:** Compared K-Means (k=4), DBSCAN (tuned), and hierarchical (Ward linkage, 3 clusters) on the same scaled coordinates via silhouette score and side-by-side geographic scatter plots: Hierarchical scored highest (0.6332), K-Means close behind (0.6248), DBSCAN lowest (0.3675).
- **Step 4 — Which method fits best:** Concluded K-Means and Hierarchical score higher because they force every point into a round, compact cluster which the silhouette metric rewards, while DBSCAN's lower score reflects its noise penalty (rural/desert points that don't belong to any dense city cluster) and its bias against elongated, non-circular real-world shapes (like coastlines) — not necessarily that it did a worse job of finding the real cities.
