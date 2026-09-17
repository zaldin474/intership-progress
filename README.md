# Internship in AI and ML at BinXTech

This repository tracks progress through an AI/ML-focused internship at **BinXTech**. It runs in two phases: a **daily-exercise phase** (Weeks 1–6), building up from core Python and the scientific-Python stack through statistics, classical machine learning, and unsupervised learning; followed by a **capstone phase** (Sprints 1–3+), an agile, sprint-based deep-learning project (heart disease prediction, then extended into image/sequence/text modalities) with its own planning docs, backlogs, and sprint reviews.

## Repo structure

```
intership-progress/
├── README.md                 <- this file
├── .gitignore
└── internship/
    ├── week1/                 <- Python & data fundamentals
    │   ├── day1/ .. day5/
    │   └── miniproject/        <- week checkpoint (copy of day5)
    ├── week2/                  <- statistics, probability & EDA
    │   ├── readme.md            <- week 2 learning objectives
    │   ├── day1/ .. day5/
    │   └── miniproject/
    ├── week3/                  <- machine learning with scikit-learn
    │   ├── day1/ .. day5/
    │   └── miniproject/
    ├── week4/                  <- model validation & generalization
    │   ├── day1/ .. day5/
    │   └── miniproject/
    ├── week5/                  <- unsupervised learning
    │   └── day1/ .. day4/
    ├── week6/
    │   └── sprint1 practice/    <- standalone practice run of the Sprint 1 baseline workflow (telco churn dataset)
    ├── project1/                <- standalone end-to-end ML project (cardiac heart disease)
    │   ├── Approach.md
    │   ├── Data/
    │   ├── Notebooks/            <- 01 data prep, 02 EDA, 03 supervised learning, 04 feature engineering pipeline, 05 unsupervised learning
    │   ├── README.md
    │   └── requirements.txt
    ├── Sprint 1/                 <- capstone: heart disease prediction — baseline + first neural network
    │   ├── plan_backlog.md
    │   ├── Data/
    │   └── notebooks/             <- baseline, activations/forward pass, training mechanics, Keras NN, tuning/close-out
    ├── Sprint 2/                 <- capstone: CNN, RNN/LSTM & Transformer exploration
    │   ├── plan.md
    │   └── notebooks/             <- CNN fundamentals, CNN + transfer learning, RNN/LSTM, Transformers, close-out
    └── Sprint 3/                  <- capstone: NLP & computer-vision preprocessing (in progress)
        └── notebooks/              <- NLP text cleaning, TF-IDF & embeddings, OpenCV image preprocessing
```

Each `dayN/` folder generally contains:
- One or more `.ipynb` notebooks with the day's exercises, mixing code cells with Markdown explanations/interpretations.
- Any dataset(s) (`.csv`) used that day, sitting alongside the notebook.
- Occasionally a standalone `.py` script alongside the notebook.
- Some days split into `practice/` (free practice) and a lab folder such as `Hands_On Lab/` (the graded/structured exercise) subfolders.

Each of Weeks 1–4 also ends with a `miniproject/` folder — a copy of that week's Day 5 notebook kept as a standalone checkpoint deliverable.

Each `Sprint N/` folder follows a sprint-based structure: a `plan.md`/`plan_backlog.md` documenting the sprint goal and backlog, a `Data/` folder (when the sprint introduces a new dataset), and a `notebooks/` folder with one notebook per sprint day, closing with a tuning/close-out notebook that compares the sprint's final model against prior baselines.

`project1/` and `Sprint 1`–`3` are self-contained pieces of work rather than daily drills — see each one's own README/plan file for the full writeup.

## Progress by phase

**Daily-exercise phase:**
- **[Week 1](internship/week1/) — Python & Data Fundamentals**: environment setup, core Python, NumPy, Pandas, and first visualizations.
- **[Week 2](internship/week2/) — Statistics, Probability & EDA**: descriptive statistics, probability simulation, linear algebra basics, outlier detection, and full exploratory data analysis.
- **[Week 3](internship/week3/) — Machine Learning with Scikit-Learn**: the standard ML workflow, Linear Regression, classification (Logistic Regression, model comparison across Decision Tree/Random Forest/SVM/KNN), and an end-to-end classification mini-project.
- **[Week 4](internship/week4/) — Model Validation & Generalization**: train/validation/test splitting, cross-validation, diagnosing/fixing overfitting and underfitting, feature engineering, hyperparameter tuning, and a leak-free end-to-end pipeline.
- **[Week 5](internship/week5/) — Unsupervised Learning**: K-Means, DBSCAN, and hierarchical clustering; dimensionality reduction with PCA and t-SNE; anomaly detection with Isolation Forest.
- **Week 6 / sprint1 practice**: a standalone practice pass through the Sprint 1 baseline workflow on a telco customer-churn dataset.

**Capstone phase (Phase 3):**
- **[project1](internship/project1/) — Cardiac Heart Disease ML Project**: a standalone end-to-end project (data prep → EDA → supervised model comparison → feature engineering & pipelines → unsupervised learning) on a synthetic 50,000-row heart disease dataset.
- **Sprint 1 — Heart Disease Prediction Baseline**: dataset EDA/cleaning, a Logistic Regression baseline, and a first Keras neural network, tuned and compared against the baseline.
- **Sprint 2 — CNNs, RNNs/LSTM & Transformers**: CNN fundamentals and transfer learning on image data, RNN/LSTM on sequential ECG data, a pretrained Transformer on text sentiment, closing with a tuned LSTM as the sprint's final model.
- **Sprint 3 — NLP & Computer Vision Preprocessing** *(in progress)*: text cleaning/TF-IDF/embeddings for NLP, and OpenCV-based image preprocessing/augmentation for computer vision.

See each week's or sprint's own README/plan file for a full day-by-day breakdown.

## Tech stack
Python, Jupyter, NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, TensorFlow/Keras, Hugging Face Transformers, NLTK, gensim, OpenCV.