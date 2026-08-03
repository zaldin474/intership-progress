# Internship in AI and ML at BinXTech

This repository tracks day-by-day progress through an AI/ML-focused internship at **BinXTech**. Each entry is a small, self-contained exercise (usually a Jupyter notebook, sometimes a standalone script) working through a specific concept — building up from core Python and the scientific-Python stack, through statistics and exploratory data analysis, into applied machine learning with scikit-learn.

## Repo structure

```
intership-progress/
├── README.md                 <- this file
├── .gitignore
└── internship/
    ├── week1/
    │   ├── day1/              <- environment setup, Jupyter workflow
    │   ├── day2/              <- core data types & control flow
    │   ├── day3/              <- NumPy
    │   ├── day4/              <- Pandas (with Hands_On Lab/ and practice/ subfolders)
    │   └── day5/               <- data cleaning & visualization (with Hands_on lab/ and practice/ subfolders)
    ├── week2/
    │   ├── readme.md           <- week 2 learning objectives
    │   ├── day1/               <- descriptive statistics
    │   ├── day2/               <- probability simulation
    │   ├── day3/               <- vectors, matrices & dot products
    │   ├── day4/               <- outlier detection & categorical data
    │   └── day5/               <- cleaning + univariate/bivariate analysis
    └── week3/
        ├── day1/                <- intro to scikit-learn
        └── day2/                <- linear regression
```

Each `dayN/` folder generally contains:
- One or more `.ipynb` notebooks with the day's exercises, mixing code cells with Markdown explanations/interpretations.
- Any dataset(s) (`.csv`) used that day, sitting alongside the notebook.
- Occasionally a standalone `.py` script alongside the notebook.
- Some days split into `practice/` (free practice) and a lab folder such as `Hands_On Lab/` (the graded/structured exercise) subfolders.

## Progress by week

- **[Week 1](internship/week1/) — Python & Data Fundamentals**: environment setup, core Python, NumPy, Pandas, and first visualizations.
- **[Week 2](internship/week2/) — Statistics, Probability & EDA**: descriptive statistics, probability simulation, linear algebra basics, outlier detection, and full exploratory data analysis (univariate + bivariate).
- **[Week 3](internship/week3/) — Machine Learning with Scikit-Learn**: the standard ML workflow, train/test splitting, and a first Linear Regression model with proper evaluation against a baseline.

See each week's own README for a day-by-day breakdown, and each day's own README for details on that day's notebook(s).

## Tech stack
Python, Jupyter, NumPy, Pandas, Matplotlib, Seaborn, scikit-learn.
