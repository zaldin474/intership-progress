# Week 1 - Day 4: Pandas — Tabular Data

## Goal
Load a real dataset into a DataFrame, inspect it, clean it, filter it, and aggregate it with `groupby`.

## What was done
- Loaded a real dataset into a DataFrame and inspected its structure.
- Selected columns and filtered rows by condition.
- Cleaned missing values and duplicates.
- Aggregated data with `groupby`.

## Folders
### `Hands_On Lab/`
Uses **`fifa_world_cup_2026_player_performance.csv`** (a Kaggle dataset) in **`jupy_day4.ipynb`**:
- **Task 1:** Loads the CSV, reports its shape, columns, and dtypes via `df.info()`.
- **Task 2:** Checks for missing values (`df.isnull().sum()` — none found), drops rows with nulls/duplicates anyway to demonstrate the pattern, with a note on why dropping (vs. filling) was the reasoned choice here.
- **Task 3:** Filters the data to meaningful subsets — players with pass accuracy ≥ 94%, then a more specific filter (England players, > 60 minutes played, > 85% pass accuracy, playing for Real Madrid/Barcelona/Manchester United) — and reports player name, team, and relevant stats.
- **Task 4:** Uses `groupby` to compute: mean tackles/interceptions/clearances/blocks by position, summed expected goals/assists/shots-on-target by team, and summed goals/assists/shots-on-target by preferred foot, each with a short interpretation of what the numbers show.

### `practice/`
Uses a generic **`data.csv`** (workout-style dataset) in **`jupy_day4.ipynb`** to practice the same fundamentals in isolation: loading/inspecting (`head`, `shape`, `info`, `describe`), selecting/filtering columns and rows (`df["Pulse"]`, `df.loc[...]`), cleaning (`isnull().sum()`, `fillna` with the column mean, `dropna`, `drop_duplicates`), and grouping/aggregating (`groupby("Duration")` with `mean` and `agg`).
