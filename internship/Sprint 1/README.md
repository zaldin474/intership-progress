# Sprint 1 — Heart Disease Prediction (Phase 3 Capstone, Week 6: Deep Learning Introduction)

Sprint 1 of the Phase 3 capstone project: build a machine-learning system that predicts `Heart Disease Status` (binary: No/Yes) from demographic, lifestyle, and clinical features — starting with a classical baseline, then progressively building, evaluating, and tuning a neural network against it.

## Contents

```
Sprint 1/
├── plan_backlog.md          <- full sprint plan, backlog, acceptance criteria & completion record
├── Data/
│   ├── heart_disease.csv     <- 10,000 rows x 21 columns
│   └── data_dictionary.md    <- column definitions
└── notebooks/
    ├── baseline.ipynb              <- Day 1: kickoff, EDA, preprocessing, Logistic Regression baseline
    ├── Neural_networks_intro.ipynb <- Day 2: activation functions, output layer/loss choice, a forward-pass experiment
    ├── Neural_networks_02.ipynb    <- Day 3: training loop, learning-rate experiments, mentor-review prep
    ├── Neural_networks_03.ipynb    <- Day 4: first Keras Sequential network, training/validation curves, regularization
    ├── Neural_networks_04.ipynb    <- Day 5: hyperparameter tuning, EarlyStopping, final model, sprint close-out
    └── best_heart_disease_model.keras  <- saved best-performing model checkpoint
```

## Dataset
`heart_disease.csv` — 10,000 patients, 21 columns (age, blood pressure, cholesterol, BMI, smoking, diabetes, exercise habits, triglycerides, fasting blood sugar, CRP, homocysteine, and more; see `Data/data_dictionary.md`). Target `Heart Disease Status` is imbalanced: ~80% No / ~20% Yes, with missing values scattered across most columns (heaviest in `Alcohol Consumption`, ~2,586 missing) and no duplicate rows.

## Day-by-day summary

- **Day 1 — Kickoff & Baseline (`baseline.ipynb`):** Confirmed the sprint goal, finalized and documented the dataset, ran a brief EDA (target distribution, numeric histograms, categorical comparisons, correlation heatmap), cleaned missing values (median for numeric, mode for categorical, with `Alcohol Consumption`'s missing values treated as a real "none" category), built a train/validation/test split, and trained a Logistic Regression baseline.
- **Day 2 — Activations & Forward Pass (`Neural_networks_intro.ipynb`):** Plotted ReLU, sigmoid, and tanh; chose and justified Sigmoid output activation with Binary Cross-Entropy loss for this binary classification task; worked a small forward-pass example by hand.
- **Day 3 — Training Mechanics & Mentor Review (`Neural_networks_02.ipynb`):** Documented the four-step training loop (forward pass → loss → backpropagation → weight update) and backpropagation conceptually; ran a learning-rate experiment comparing a too-low (0.00001), reasonable (0.001), and too-high (0.5) rate on the same tiny network, plotting loss curves for each.
- **Day 4 — Keras Neural Network (`Neural_networks_03.ipynb`):** Preprocessed features with a `ColumnTransformer` (StandardScaler + one-hot encoding), built and compiled a first Keras Sequential network (Dense(64) → Dense(32) → Dense(1, sigmoid)) with the Adam optimizer, trained with a validation split, plotted training/validation curves, and added regularization (dropout/batch normalization).
- **Day 5 — Tuning & Sprint Close-Out (`Neural_networks_04.ipynb`):** Tuned hyperparameters one at a time (learning rate, architecture, dropout, batch size), added `EarlyStopping` and `ModelCheckpoint` to preserve the best weights, and assembled the final baseline-vs-neural-network comparison.

## Results

| Model | Test Accuracy | Macro F1 | Yes Precision | Yes Recall | Main finding |
|---|---:|---:|---:|---:|---|
| Logistic Regression | 0.800 | 0.444 | 0.000 | 0.000 | Majority-class collapse; accuracy is misleading |
| Balanced Logistic Regression | 0.504 | ~0.45 | 0.19 | 0.458 | Detects positives, but many false positives |
| Regularized Neural Network | 0.798 | 0.444 | 0.000 | 0.000 | Regularization alone did not solve class imbalance |
| Regularized + Class-Balanced NN | 0.518 | 0.463 | 0.207 | 0.500 | Best positive-class recall among the NN runs |
| Final Tuned NN | 0.685 | 0.501 | 0.202 | 0.195 | Best macro F1, but recall dropped vs. the balanced NN |

**Conclusion:** the core challenge was the 80/20 class imbalance — plain accuracy consistently overstated performance, since a model could score ~80% just by always predicting "No." Class weighting improved minority-class (positive) detection; tuning improved macro F1 to ~0.501 but traded away much of the recall gained by the balanced network. Model choice should depend on the project's actual objective (e.g. catching more true positives vs. overall balanced performance) rather than on accuracy alone.

## Known follow-ups (from the sprint's own review notes)
A few items were flagged in `plan_backlog.md` for correction/verification before mentor review: missing-value imputation is currently fit on the full dataset rather than training data only (risk of leakage), the `Alcohol Consumption` → "none" mapping should be confirmed against the dataset's actual documentation, baseline ROC-AUC still needs to be added, and the final reported model should be evaluated directly from the saved checkpoint (`best_heart_disease_model.keras`) to guarantee the reported score matches the saved artifact.

See `plan_backlog.md` for the full backlog, acceptance criteria, Git/PR workflow, and sprint retrospective.