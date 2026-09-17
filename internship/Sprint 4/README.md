# Sprint 4 - Model Deployment

## Project Overview

Sprint 4 focused on converting the completed IMDb sentiment classification model into a usable and publicly deployed application.

The final system accepts a movie review and predicts whether its sentiment is positive or negative.

The deployed application uses:

- Text preprocessing with NLTK
- TF-IDF feature extraction
- Logistic Regression classification
- FastAPI for API serving
- Streamlit for the user interface
- Render for public deployment

---

## Model

The final model is a TF-IDF + Logistic Regression sentiment classifier trained on the IMDb 50K Movie Reviews dataset.

Final evaluation results:

| Metric | Score |
|---|---:|
| Accuracy | 0.888 |
| Precision | 0.879 |
| Recall | 0.901 |
| F1-score | 0.890 |

The serialized model reproduced the same results after being saved and loaded again, confirming that serialization was successful.

---

## Sprint 4 Work

### Day 1 - Serialization & Reproducibility

The trained Logistic Regression model and fitted TF-IDF vectorizer were serialized using `joblib`.

Saved artifacts:

- `sentiment_model.joblib`
- `tfidf_vectorizer.joblib`

The saved objects were loaded again and verified to reproduce the same model performance.

---

### Day 2 - FastAPI

A FastAPI REST API was created with a `/predict` endpoint.

The API:

- Accepts raw movie reviews.
- Validates requests using Pydantic.
- Applies text preprocessing.
- Applies the saved TF-IDF vectorizer.
- Loads the serialized Logistic Regression model.
- Returns the predicted sentiment and confidence score.

The endpoint was tested successfully through FastAPI `/docs`, including invalid-input validation.

---

### Day 3 - Streamlit Dashboard

A Streamlit dashboard was created for non-technical users.

The interface includes:

- Movie review text input.
- Sentiment prediction.
- Prediction confidence.
- Probability visualization.
- Empty-input validation.

Positive, negative, and empty-input cases were tested successfully.

---

### Day 4 - Public Deployment

The Streamlit application was deployed publicly using Render.

Live application:

https://imdb-review-sentiment-predictor.onrender.com/

The deployed application was tested to confirm that its predictions matched the local version.

---

## Prediction Pipeline

```text
Movie Review
    ↓
Input Validation
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Logistic Regression
    ↓
Sentiment Prediction
    ↓
Confidence + Probability Visualization
```

---

## Repository Structure

```text
Sprint 4/
├── Data/
│   └── IMDB Dataset of 50K Movie Reviews/
├── notebooks/
│   ├── 01_Serialization/
│   │   ├── 01_Serialization_MLOps.ipynb
│   │   └── model/
│   ├── 02_FastApi/
│   │   ├── main.py
│   │   ├── preprocessing.py
│   │   └── README.md
│   └── 03_Streamlit/
│       ├── app.py
│       ├── preprocessing.py
│       ├── requirements.txt
│       ├── README.md
│       └── model/
├── Plan.md
└── README.md
```

---

## Setup

### Install dependencies

For the Streamlit application:

```bash
pip install -r requirements.txt
```

### Run the Streamlit app locally

```bash
python -m streamlit run app.py
```

### Run the FastAPI service locally

```bash
python -m uvicorn main:app --reload
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## Limitations

The current model uses TF-IDF, which does not fully capture:

- Word order
- Sarcasm
- Complex context
- Mixed sentiment
- Context-dependent word meanings

The model can also produce incorrect predictions for ambiguous or unusual reviews.

---

## Future Improvements

Possible improvements include:

- Fine-tuning a Transformer model directly on the IMDb dataset.
- Adding richer explainability to the Streamlit application.
- Improving confidence calibration.
- Adding more robust input handling.
- Separating the API and UI into a production-style architecture.

---

## Conclusion

Sprint 4 successfully converted the trained IMDb sentiment classification model into a complete deployed application.

The model was serialized, served through FastAPI, integrated into a Streamlit dashboard, and deployed publicly using Render.

The final result is a working end-to-end machine learning application that can be accessed and tested by real users.