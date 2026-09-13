# Sprint 4 Plan - Model Deployment

## Sprint Goal

The goal of Sprint 4 is to convert the completed IMDb sentiment classification model into a usable and publicly deployed application.

The final system should allow a user to enter a movie review and receive a sentiment prediction through a web interface.

---

## Day 1 - Serialization & Reproducibility

- Save the trained Logistic Regression model using `joblib`.
- Save the fitted TF-IDF vectorizer.
- Load both objects again and verify that they reproduce the same prediction.
- Create a pinned `requirements.txt`.
- Keep fixed random seeds for reproducibility.

### Deliverables

- `sentiment_model.joblib`
- `tfidf_vectorizer.joblib`
- `requirements.txt`
- Serialization test completed successfully.

---

## Day 2 - FastAPI Model Serving

- Create a FastAPI application.
- Load the saved model and TF-IDF vectorizer.
- Create a `/predict` POST endpoint.
- Use Pydantic to validate incoming review text.
- Return the sentiment prediction and confidence as JSON.
- Test the API locally using `/docs`.

---

## Day 3 - Streamlit Dashboard

- Build a simple Streamlit interface.
- Add a text area for movie reviews.
- Send the review through the prediction pipeline.
- Display the predicted sentiment and confidence.
- Add one supporting visualization if useful.
- Test the application locally.

---

## Day 4 - Public Deployment

- Choose a hosting platform.
- Prepare the deployment files.
- Verify `requirements.txt`.
- Upload the model and preprocessing files.
- Deploy the application publicly.
- Test several reviews on the live version.
- Confirm live predictions match local predictions.

---

## Day 5 - Repository Polish & Sprint Close-Out

- Clean the repository structure.
- Update the README.
- Add setup and usage instructions.
- Add the public deployment URL.
- Document model results and limitations.
- Check the project against the Definition of Done.
- Complete the Sprint 4 retrospective.

---

## Final Sprint 4 Deliverables

- Serialized model and TF-IDF vectorizer.
- Working FastAPI prediction endpoint.
- Interactive Streamlit dashboard.
- Publicly deployed application.
- Pinned `requirements.txt`.
- Clean GitHub repository.
- Updated README and technical documentation.
- Sprint 4 retrospective.


# Possible Folder Structure:

Sprint 4/
├──Data
│   └── IMDB Dataset of 50k Movie reviews
├── PLAN.md
├── 01_Serialization_MLOps.ipynb
├── requirements.txt
├── model/
│   ├── sentiment_model.joblib
│   └── tfidf_vectorizer.joblib
├── api/
│   └── main.py
└── app/
    └── streamlit_app.py