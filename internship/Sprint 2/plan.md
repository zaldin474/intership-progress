# Sprint 2 Plan — Image Waste Classification

## Sprint Goal

Develop and improve an image-classification model capable of distinguishing the waste categories in the Plastic - Paper - Garbage Bag Synthetic Images dataset.

Since the project uses image data, a **Convolutional Neural Network (CNN)** will be used as the main architecture.

The sprint will compare a CNN trained from scratch, regularization/data augmentation, and transfer learning to identify the strongest approach.

---

## Dataset

**Dataset:** Plastic - Paper - Garbage Bag Synthetic Images
**Data Type:** Images
**Task:** Multi-class image classification
**Core Architecture:** CNN

---

## Sprint 1 Improvement Carried Forward

Experiments will be documented from the beginning with their configuration and evaluation metrics so that model comparisons remain clear and reproducible.

---

## Sprint Backlog

### Day 1 — CNN Fundamentals

* [ ] Inspect dataset structure and class distribution.
* [ ] Display sample images from each class.
* [ ] Apply a hand-defined edge-detection filter.
* [ ] Visualize the resulting feature map.
* [ ] Explain convolution and parameter sharing.
* [ ] Confirm CNN as the project architecture.

### Day 2 — CNN & Transfer Learning

* [ ] Preprocess and split the image dataset.
* [ ] Build a CNN from scratch.
* [ ] Train and evaluate the CNN.
* [ ] Add data augmentation.
* [ ] Compare validation curves before and after augmentation.
* [ ] Apply transfer learning using a pre-trained CNN.
* [ ] Compare accuracy and other evaluation metrics.

### Day 3 — RNN & LSTM Learning

* [ ] Study RNN and LSTM concepts.
* [ ] Complete the required sequential-data demonstration.
* [ ] Explain why RNN/LSTM is not appropriate for the image project.
* [ ] Prepare notebook/code for mentor review.

### Day 4 — Attention & Transformers

* [ ] Study attention and Transformer concepts.
* [ ] Complete the required pre-trained Transformer demonstration.
* [ ] Explain why Transformers are not the selected core architecture for this image project.

### Day 5 — Core Model & Sprint Review

* [ ] Select the strongest CNN approach.
* [ ] Tune the core model.
* [ ] Record final training and validation curves.
* [ ] Evaluate the final model on the test set.
* [ ] Create a metric comparison table.
* [ ] Compare the final model with earlier experiments.
* [ ] Complete Sprint Review.
* [ ] Write Sprint 2 Retrospective.

---

## Acceptance Criteria

Sprint 2 is complete when:

* The dataset is inspected and documented.
* A convolution demonstration and feature map are included.
* A CNN is built and trained successfully.
* Data augmentation is tested.
* Transfer learning is tested.
* Experiments and metrics are recorded.
* The final model is evaluated on unseen test data.
* Model results are compared in a clear table.
* Notebook explanations are written in Markdown.
* Sprint Review and Retrospective are completed.

---

## Expected Model Progression

Basic CNN
↓
CNN + Data Augmentation
↓
Transfer Learning
↓
Tuning / Regularization
↓
Final Core Model

---

## Main Evaluation Metrics

The project will record:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Training Loss
* Validation Loss

The final model will be selected based on overall validation and test performance rather than a single metric.
