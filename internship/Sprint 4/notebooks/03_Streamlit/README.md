# Day 3 - Streamlit Sentiment Dashboard

## Hands-On Lab

The Day 3 hands-on lab focused on building an interactive Streamlit interface for the IMDb sentiment classification model.

The required tasks were:

1. Build a Streamlit app that loads the trained model and preprocessing objects.
2. Accept user input through an appropriate widget.
3. Run the model on the user input and display the prediction clearly.
4. Add a supporting visualization.
5. Test the application locally and confirm that a first-time user can use it easily.

---

## What Was Implemented

The Streamlit application loads:

- The serialized Logistic Regression sentiment model.
- The fitted TF-IDF vectorizer.
- The same text preprocessing function used during training.

The interface includes:

- A text area for entering a movie review.
- A prediction button.
- The predicted sentiment.
- A confidence score.
- A probability bar chart.
- Input validation for empty reviews.

The prediction flow is:

```text
Movie Review
    ↓
Input Validation
    ↓
Text Preprocessing
    ↓
TF-IDF Transformation
    ↓
Logistic Regression Model
    ↓
Sentiment Prediction
    ↓
Confidence + Probability Chart
```

---

## Test Case 1 - Positive Review

### Input

```text
This movie was amazing and I really enjoyed it.
```

### Response

```text
Prediction: Positive ✅
Confidence: 99.73%
```

### Result

The model correctly classified the review as **positive** with approximately **99.73% confidence**.

---

## Test Case 2 - Negative Review

### Input

```text
This movie was boring, badly written, and a waste of time.
```

### Response

```text
Prediction: Negative ❌
Confidence: 99.97%
```

### Result

The model correctly classified the review as **negative** with approximately **99.97% confidence**.

---

## Test Case 3 - Empty Review

### Input

```text

```

### Response

```text
Please enter a movie review first !
```

### Result

The application correctly rejected the empty input and did not send it to the prediction pipeline.

This confirms that the input validation works correctly and prevents meaningless predictions for empty reviews.

---

## Supporting Visualization

A probability bar chart was added to display the prediction probabilities for the sentiment classes.

This gives the user more information than only showing the final label and makes the prediction easier to interpret.

---

## Overall Result

The Streamlit application successfully:

- Accepted movie reviews from the user.
- Applied the same preprocessing used during training.
- Used the saved TF-IDF vectorizer.
- Used the serialized Logistic Regression model.
- Displayed positive and negative predictions correctly.
- Displayed prediction confidence.
- Displayed class probabilities in a bar chart.
- Rejected empty reviews before prediction.

---

## Conclusion

The IMDb sentiment classification model was successfully integrated into a Streamlit dashboard.

The application provides a simple interface where a user can enter a movie review and receive a sentiment prediction together with a confidence score and probability visualization.

The app was tested with positive, negative, and empty inputs. Valid reviews produced the expected predictions, while empty input was handled correctly through validation.

This completes the Day 3 Streamlit hands-on lab and prepares the project for public deployment in Day 4.