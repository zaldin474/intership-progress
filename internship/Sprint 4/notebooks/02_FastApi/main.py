from fastapi import FastAPI
from pydantic import BaseModel
import joblib

from preprocessing import preprocess_text
from pathlib import Path

# Build reliable paths
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR
    / ".."
    / "01_Serialization"
    / "model"
    / "sentiment_model.joblib"
).resolve()

TFIDF_PATH = (
    BASE_DIR
    / ".."
    / "01_Serialization"
    / "model"
    / "tfidf_vectorizer.joblib"
).resolve()

# verify path
print("Model path:", MODEL_PATH)
print("Exists:", MODEL_PATH.exists())

print("TF-IDF path:", TFIDF_PATH)
print("Exists:", TFIDF_PATH.exists())


# 1. Load saved model and vectorizer (using joblib)
loaded_model = joblib.load(MODEL_PATH)

loaded_tfidf = joblib.load(TFIDF_PATH)


# 2. Create FastAPI app
app = FastAPI(
    title="IMDB sentiment prediction Api",
    description="predicts wheter a movie review is positive or negative",
    version="1.0"
    )

# 3. Define input schema (with pydantic)
class Review_Input(BaseModel):
    review:str


# 4. Root endpoint
@app.get("/")

def root():
    return{"message":"IMDB sentiment prediction Api is running"}


# 5. Prediction endpoint
@app.post("/predict")

def predict(data: Review_Input):
    
    # clean (preprocess) text first
    cleaned_review = preprocess_text(data.review)
    
    # Transform review using saved TF-IDF vectorizer
    vectorized_review = loaded_tfidf.transform([cleaned_review])
    
    # Predict sentiment
    prediction = loaded_model.predict(vectorized_review)[0]
    
    # Get prediction probabilities
    probabilities  = loaded_model.predict_proba(vectorized_review)[0]
    
    confidence = probabilities.max()

    return {
        "review": data.review,
        "prediction": prediction,
        "confidence": float(confidence)
     }
    
    
    ### run it through:
    # activating venv
    # running python -m uvicorn main:app --reload 
    # going to the url address it gives 