# Week 2 - Day 1: Descriptive Statistics

## Goal (from `internship/week2/readme.md`)
1. Compute mean, median, and mode, and choose the appropriate one for a given dataset.
2. Compute and interpret variance, standard deviation, and IQR.
3. Explain how outliers affect each measure differently.

## What was done
Working with **`k-means.csv`** (a dataset with an `income` column) in **`jupy_day1.ipynb`**:
- Computed `mean`, `median`, and `mode` (mode approximated via `np.median` here), along with `max`/`min` of the `income` column.
- Computed standard deviation, variance, and the IQR (25th/75th percentiles and their difference).
- Discussed when each central-tendency measure is appropriate: the mean is best for unskewed data without outliers, while the median is more robust when the data is skewed or contains outliers.
- Interpreted the results for this dataset: income is best represented by the median/mode (~67,500) rather than the mean (~90,432), since the mean is pulled higher by right-skew; the data ranges from 45,000 to 162,000, the IQR is 76,750, and the standard deviation (~42,505) confirms a wide spread.
