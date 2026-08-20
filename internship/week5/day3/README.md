# Week 5 - Day 3: Dimensionality Reduction with PCA

## Goal
Scale a high-dimensional dataset, fit PCA, choose a number of components that retains ~95% of variance, reduce to 2D for visualization, and document what was gained and lost.

## Dataset
`cardiac arrest dataset-selected-columns.csv` (with an accompanying `data dictionary.md`) — 10 features plus a `target` column; duplicates checked and removed before analysis.

## What was done (`jupy_day3.ipynb`)
- **Step 1 — Scaling:** Standardized the 10 features with `StandardScaler` after separating `target`.
- **Step 2 — Explained variance:** Fit PCA and plotted cumulative explained variance against the number of components.
- **Step 3 — Choosing components:** Looped over 1–10 components to find the smallest number retaining ~95% variance, settling on **9 components at 96.41%** — noting that keeping all 10 would retain 100% but defeat the purpose of dimensionality reduction.
- **Step 4 — 2D visualization:** Reduced to 2 principal components and inspected a heatmap of the `pca.components_` matrix (each row a component, each column an original feature) to see which original features contribute most to each principal component.
- **Step 5 — What was preserved/cost:** Documented that PCA captures the directions of greatest variance in order (first component = most variance, subsequent components orthogonal to prior ones), and that reducing to fewer components trades off some of the original variance/information for a lower-dimensional, more visualizable representation.
