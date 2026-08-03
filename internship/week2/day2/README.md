# Week 2 - Day 2: Probability Simulation

## Goal
Use NumPy to simulate randomness and connect simulation results to probability theory.

## What was done (`jupy_day2.ipynb`)
- **Task 1:** Simulated 10,000 coin flips with `np.random.rand` rounded to 0/1, confirming the proportion of heads approaches 0.5.
- **Task 2:** Drew samples from a normal distribution with `np.random.normal` and plotted a histogram to confirm the bell shape.
- **Task 3:** Worked a conditional-probability scenario by hand (probability of rolling a 5 given the roll is odd, i.e. 1 in 3) and verified it with a 10,000-roll simulation using `np.random.randint`, getting a result close to the theoretical 1/3 (0.3375).
