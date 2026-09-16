'''
Hands-On Lab: Building the Demo + Mentor Review
● Step 1: Build a Streamlit app that loads the model and takes the project's inputs via appropriate widgets.
● Step 2: Run the model on user input and display the prediction prominently.
● Step 3: Add one supporting visualization (probability, SHAP explanation, or the uploaded image).
● Step 4: Run the app locally and confirm a first-time user can get a prediction easily.
● Step 5: Open a pull request with the deployment code for the mid-sprint Mentor Code Review and address the feedback.
'''

import streamlit as st 
import joblib
from pathlib import Path

from preprocessing import preprocess_text

# ============================================
# 1. Paths
# ============================================
BASE_DIR = Path(__file__).resolve().parent

# the same models made by day 1 serializations
MODEL_PATH = (
    BASE_DIR 
    / "model"
    / "sentiment_model.joblib"
).resolve()

TFIDF_PATH = (
    BASE_DIR 
    / "model"
    / "tfidf_vectorizer.joblib"
).resolve()

# ============================================
# 2. Load model and vectorizer
# ============================================
loaded_model = joblib.load(MODEL_PATH)
Loaded_tfidf = joblib.load(TFIDF_PATH)


# ============================================
# 3. Page configuration
# ============================================

st.set_page_config(
    page_title="IMDB Sentiment Predictor",
    page_icon= "🎬",
    layout= "centered"
)

# ============================================
# 4. Title and description
# ============================================
st.title("🎬 IMDB Sentiment Predictor")

st.write ("Enter a movie review below and the model will predict "
    "whether the sentiment is positive or negative.")

# ============================================
# 5. User input
# ============================================
review = st.text_area(
    "Movie Review",
    placeholder=("Type your review here..."),
    height=180
)

# ============================================
# 6. Prediction button
# ============================================

if st.button("Predict Sentiment"):
    
    if review.strip() == "":
        
        st.warning("Please enter a movie review first !")
        
    else:
        # clean text 
        cleaned_review = preprocess_text(review)
        
        # tfidf transfrom
        vectorized_review = Loaded_tfidf.transform([cleaned_review])
        
        # prediction
        prediction = loaded_model.predict (vectorized_review)[0]
        
        # probabilities
        probabilities = loaded_model.predict_proba(vectorized_review)[0]
        
        confidence = probabilities.max()
        
        # ====================================
        # 7. Display prediction
        # ====================================
        
        if prediction == "positive":

            st.success(
                f"Prediction: Positive ✅"
            )

        else:

            st.error(
                f"Prediction: Negative ❌"
            )


        st.write(
            f"Confidence: {confidence:.2%}"
        )
        
        # ====================================
        # 8. Probability visualization
        # ====================================

        classes = loaded_model.classes_

        probability_dict = {classes[i]:  probabilities[i] for i in range(len(classes))}

        st.write("### Prediction Probabilities")

        st.bar_chart( probability_dict)
        
        
        
        
        
# to run:
# activate venv while in 03_streamlit
# then run python -m streamlit run app.py