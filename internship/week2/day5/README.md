# Week 2 - Day 5: Data Cleaning & Univariate/Bivariate Analysis

## Goal
Practice a full exploratory data analysis pass: cleaning/renaming a real dataset, then exploring it with univariate and bivariate visualizations.

## Dataset
`coaster_db.csv` — roller coaster records (name, location, status, manufacturer, speed, height, G-force, inversions, dates, etc.).

## What was done (`jupy_day5.ipynb`)
### Data preparation
- Subset the dataframe to the relevant columns, converted `opening_date` to a proper datetime type, and renamed columns for consistency (e.g. `coaster_name` → `Coaster_Name`).
- Checked for missing values and for duplicates — first exact duplicate rows, then duplicates by name only, then duplicates by name + location + opening date (the true duplicate key) — and dropped the true duplicates, resetting the index.

### Univariate analysis
- Used `value_counts()` on `Year_Introduced` to find the most common opening years, then plotted the top 10 as a bar chart (2000 and 1999 each had 40+ new coasters).
- Plotted histograms and KDE (kernel density) plots for `Speed_mph` and `Gforce` to see their distributions.

### Bivariate analysis
- **Pair plot:** plotted every numeric variable against every other in one grid.
- **Correlation heatmap:** computed the correlation matrix and visualized it, finding a strong positive correlation between speed and height (+0.82), almost none between latitude and inversions, and a slight negative correlation between latitude and longitude.
- **Scatter plots:** speed vs. height and speed vs. G-force, both showing a positive relationship (faster coasters tend to be taller and pull more G-force).
- **Box plots:** speed by coaster material type (steel coasters show more spread and higher max speeds) and height by rounded G-force (showing the typical height range for common G-force values).
