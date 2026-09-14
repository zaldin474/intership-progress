# Day 2 - FastAPI Prediction API

## Hands-On Lab

The Day 2 hands-on lab focused on serving the trained IMDb sentiment classification model through a FastAPI REST API.

The required tasks were:

1. Load the serialized model and preprocessing objects from Day 1.
2. Define an input schema using Pydantic.
3. Implement a `/predict` POST endpoint.
4. Run the FastAPI server locally and test it through the `/docs` interface with several inputs.
5. Confirm that invalid input is rejected cleanly by Pydantic.

---

## What Was Implemented

The FastAPI application loads:

- The serialized Logistic Regression sentiment model.
- The fitted TF-IDF vectorizer.
- The same text preprocessing function used during training.

The `/predict` endpoint accepts a movie review, preprocesses it, transforms it into TF-IDF features, passes it to the trained Logistic Regression model, and returns:

- The original review.
- The predicted sentiment.
- The confidence score.

Pydantic is used to validate the incoming request and make sure that the required `review` field is included.

The prediction flow is:

```text
User Request
    ↓
Pydantic Validation
    ↓
Text Preprocessing
    ↓
TF-IDF Transformation
    ↓
Logistic Regression Model
    ↓
Prediction + Confidence
    ↓
JSON Response
```

---

# API Testing

The API was tested through FastAPI's automatically generated `/docs` interface.


INFO:     127.0.0.1:51870 - "POST /predict HTTP/1.1" 200 OK 

INFO:     127.0.0.1:49260 - "POST /predict HTTP/1.1" 200 OK 

INFO:     127.0.0.1:51595 - "POST /predict HTTP/1.1" 422 Unprocessable Entity


## Test Case 1 - Positive Review

### Input

```json
{
  "review": "This movie was amazing and I really enjoyed it."
}
```

### Response

```json
{
  "review": "This movie was amazing and I really enjoyed it.",
  "prediction": "positive",
  "confidence": 0.9973436644975928
}
```

### Result

The API correctly classified the review as **positive**.

The model returned a confidence score of approximately **99.73%**, showing that it was highly confident in the positive prediction.

---

## Test Case 2 - Negative Review

### Input

```json
{
  "review": "This movie was boring, badly written, and a waste of time."
}
```

### Response

```json
{
  "review": "This movie was boring, badly written, and a waste of time.",
  "prediction": "negative",
  "confidence": 0.9997262166915324
}
```

### Result

The API correctly classified the review as **negative**.

The model returned a confidence score of approximately **99.97%**, showing that it was highly confident in the negative prediction.

---

## Test Case 3 - Invalid Input

### Input

```json
{}
```

### Response

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "body",
        "review"
      ],
      "msg": "Field required",
      "input": {}
    }
  ]
}
```

### Result

FastAPI returned an **Unprocessable Entity** error because the required `review` field was missing.

The request was rejected before reaching the prediction pipeline.

This confirms that Pydantic validation is working correctly and that invalid input is handled safely instead of causing the application to fail.

---

## Overall Result

The FastAPI prediction service successfully handled all tested cases.

- Positive reviews were classified correctly.
- Negative reviews were classified correctly.
- Confidence scores were returned for valid predictions.
- Invalid input was rejected automatically by Pydantic.
- The serialized Logistic Regression model was loaded successfully.
- The saved TF-IDF vectorizer was reused successfully.
- The same preprocessing pipeline used during training was applied during prediction.
- The model was served without retraining it inside the API.

This confirms that the complete prediction pipeline works correctly:

```text
Raw Movie Review
        ↓
Input Validation
        ↓
Text Cleaning
        ↓
TF-IDF Vectorization
        ↓
Logistic Regression
        ↓
Positive / Negative Prediction
        ↓
Confidence Score
```

---

## Conclusion

The IMDb sentiment classification model was successfully served through a FastAPI REST API.

The `/predict` endpoint accepts raw movie reviews, validates the input using Pydantic, applies the same preprocessing used during training, transforms the review using the saved TF-IDF vectorizer, and returns a sentiment prediction together with a confidence score.

The API was tested with both positive and negative movie reviews and produced the expected predictions with very high confidence.

Invalid input was also tested by sending an empty request body. Pydantic correctly rejected the request because the required `review` field was missing.

Overall, the Day 2 FastAPI hands-on lab was completed successfully. The trained model can now be accessed through an API instead of only from a notebook, preparing the project for the Day 3 Streamlit user interface.