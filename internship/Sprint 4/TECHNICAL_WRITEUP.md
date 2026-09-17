# Technical Write-Up - IMDb Sentiment Classification

## Problem

The goal of the project is to classify IMDb movie reviews as either positive or negative sentiment.

The final system should accept raw text from a user and return a sentiment prediction with a confidence score.

---

## Dataset

The project uses the IMDb Dataset of 50K Movie Reviews.

The dataset contains labeled positive and negative movie reviews and was used for training and evaluating the sentiment classifier.

---

## Preprocessing

The text preprocessing pipeline includes:

- Tokenization
- Lowercasing
- Punctuation removal
- Stop-word removal
- Lemmatization

Negation words such as `not`, `no`, and `nor` were preserved because they are important for sentiment classification.

---

## Feature Representation

TF-IDF was used to convert cleaned text into numerical features.

The vectorizer was fitted only on the training data and reused during testing and deployment to prevent training/serving skew.

---

## Model

A Logistic Regression classifier was trained using the TF-IDF features.

Final model performance:

| Metric | Score |
|---|---:|
| Accuracy | 0.888 |
| Precision | 0.879 |
| Recall | 0.901 |
| F1-score | 0.890 |

The serialized model reproduced the same evaluation results after being loaded again.

---

## Deployment

The model was deployed through two interfaces:

### FastAPI

A REST API exposes a `/predict` endpoint that accepts a movie review and returns:

- Sentiment
- Confidence score

Pydantic is used for request validation.

### Streamlit

A Streamlit dashboard provides a user-friendly interface with:

- Text input
- Prediction output
- Confidence score
- Probability visualization

The Streamlit application was deployed publicly using Render.

---

## Live Application

https://imdb-review-sentiment-predictor.onrender.com/

---

## Limitations

TF-IDF does not fully capture word order or contextual meaning.

This can make the model less effective for:

- Sarcasm
- Mixed sentiment
- Complex language
- Context-dependent expressions

---

## Future Work

Future improvements could include:

- Fine-tuning DistilBERT directly on the IMDb dataset.
- Adding SHAP-based explanations to the deployed application.
- Improving confidence calibration.
- Adding automated tests for the deployment pipeline.

---

## Conclusion

The project demonstrates the full machine learning workflow from preprocessing and training to evaluation, serialization, API serving, user-interface development, and public deployment.

The final application provides a working sentiment prediction service that can be accessed through a public URL.