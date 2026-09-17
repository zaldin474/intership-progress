# Sprint 4 & Full Project Retrospective

## Definition of Done

| Requirement | Status | Evidence |
|---|---|---|
| Full ML pipeline | ✅ | Preprocessing, training, evaluation, serialization and deployment completed |
| Reproducible benchmark | ✅ | Final model metrics documented |
| Serialized model | ✅ | Logistic Regression and TF-IDF vectorizer saved with joblib |
| FastAPI service | ✅ | `/predict` endpoint implemented and tested |
| Streamlit dashboard | ✅ | Interactive dashboard completed |
| Public deployment | ✅ | Render deployment is live |
| Input validation | ✅ | FastAPI and Streamlit validation tested |
| Requirements documented | ✅ | Deployment requirements file included |
| Repository documentation | ✅ | README files and technical write-up included |
| Model limitations documented | ✅ | Limitations and future work documented |

---

## What Went Well

- The model and preprocessing pipeline were successfully serialized.
- The saved model reproduced the original model's performance.
- FastAPI successfully exposed the model through a REST endpoint.
- Streamlit provided a simple interface for non-technical users.
- Positive, negative, and invalid inputs were handled correctly.
- The final Streamlit application was deployed publicly using Render.

---

## Challenges

- Managing relative file paths between different Sprint 4 folders caused some issues.
- The deployment environment required a smaller and cleaner `requirements.txt`.
- Streamlit required additional input validation to prevent empty reviews from being classified.
- Local development and deployed environments needed consistent preprocessing and model files.

---

## What I Would Improve

If the project were continued, I would:

- Create a shared preprocessing module instead of keeping separate copies.
- Fine-tune a Transformer directly on the IMDb dataset.
- Add automated API and UI tests.
- Improve the repository structure further.
- Add model explainability to the deployed Streamlit interface.

---

## Main Learning Outcome

The biggest lesson from Sprint 4 was that building a machine learning model is only one part of a complete ML project.

A production-ready workflow also requires:

- Reproducible preprocessing.
- Model serialization.
- API serving.
- User interface development.
- Dependency management.
- Deployment.
- Input validation.
- Documentation.

---

## Final Result

The Phase 3 project now has a complete end-to-end workflow:

```text
Raw Review
    ↓
Preprocessing
    ↓
TF-IDF
    ↓
Logistic Regression
    ↓
FastAPI / Streamlit
    ↓
Public Render Deployment
```

The final application is available at:

https://imdb-review-sentiment-predictor.onrender.com/