# Week 1 - Day 1: Environment Setup & the Jupyter Workflow

## Goal
Set up a working Python data-science environment and get comfortable with the Jupyter workflow.

## What was done
- Installed the core data/ML libraries: `pandas`, `matplotlib`, `numpy`, `jupyter`.
- Created an isolated Python environment for the internship work.
- Froze the environment's dependencies into `requirements.txt` for reproducibility.
- Initialized this GitHub repository to track daily progress.

## Files
- **`jupy_day1.ipynb`** — Notebook confirming the environment works (`pip install pandas`, a `print("hello")` sanity check), then a small demo of simple arithmetic: a compound-interest calculator, first with hardcoded values and then rewritten to take interest rate, initial amount, and number of periods as user input.
- **`Week1_day1.py`** — Standalone script with two small functions: `check_even_odd(num)` (returns whether a number is even/odd) and `factorial(n)` (recursive factorial), run over a sample list of values in `main()`.
- **`requirements.txt`** — Frozen list of installed package versions (numpy, pandas, matplotlib, and their dependencies) for recreating the environment.
