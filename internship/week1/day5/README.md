# Week 1 - Day 5: Data Cleaning & Visualization

## Goal
Clean a dataset with Pandas, derive a numeric feature with NumPy, and build labeled visualizations (histogram, scatter, line plot) that are then interpreted in writing.

## Folders
### `Hands_on lab/`
Uses **`data.csv`** (a workout dataset with Pulse/Calories/Duration) in **`jupy_day5.ipynb`**:
- **Task 1 — Cleaning:** Checks for missing values (3 found), drops those rows since they're few enough not to affect data integrity, fills remaining `Calories` NaNs with the column mean, fixes an outlier `Duration` value of 450 (treated as a typo, corrected to 45), and drops duplicates.
- **Task 2 — Derived feature:** Uses `np.divide` to compute a new `Cal_Per_Min` column (calories burned per minute) and summarizes it with `.describe()`.
- **Task 3 — Visualizations:** Builds three labeled subplots — a histogram of pulse rate, a scatter plot of average pulse vs. calories, and a line plot of calories burned over time.
- **Task 4 — Interpretation:** Markdown analysis noting pulse rate clusters around 95–110 BPM, a moderate positive correlation between average pulse and calories burned, and relatively stable daily calorie burn (250–400) across December.
- The notebook also keeps an earlier "ignore this, practice only" section with extra histogram/scatter/line-plot experiments that fed into the final task.

### `practice/`
**`jupy_day5.ipynb`** — General Matplotlib practice: a simple line plot, comparing scatter/bar/histogram chart types on the same data, and building subplots (single-axes and side-by-side multi-axes figures).
