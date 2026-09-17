# Sprint 3 — NLP & Computer Vision Preprocessing (In Progress)

Sprint 3 continues the deep-learning track, splitting into two data-modality tracks: text preprocessing/vectorization (NLP) and image preprocessing (Computer Vision with OpenCV). No `plan.md` has been added yet for this sprint, and as of now only the first three days' notebooks are present.

## Contents

```
Sprint 3/
└── notebooks/
    ├── 01_NLP_preprocessing.ipynb        <- Day 1: tokenization, cleaning pipeline (IMDb reviews)
    ├── 02_TF-IDF & Embeddings.ipynb       <- Day 2: TF-IDF baseline, GloVe embeddings, vs. Sprint 2 Transformer
    └── 03_C.-Vis. Preprocessing_OpenCV.ipynb  <- Day 3: OpenCV image preprocessing & augmentation
```

## Notebook summaries

- **`01_NLP_preprocessing.ipynb` — Text Cleaning:** Reused the IMDb 50K movie reviews dataset (from Sprint 2, Day 4), dropped duplicates, and built a full text-cleaning pipeline demonstrated step-by-step on one review — tokenization (`word_tokenize`), lowercasing, punctuation removal, stop-word removal (deliberately keeping negation words like "not"/"no"/"nor" since they matter for sentiment), and lemmatization — then applied the pipeline as one function across the full dataset.
- **`02_TF-IDF & Embeddings.ipynb` — Vectorizing Text:** Re-ran the Day 1 cleaning pipeline, then vectorized the cleaned reviews with `TfidfVectorizer` (fit on training data only) and trained a Logistic Regression baseline (91.5% accuracy, macro F1 ~0.91 on a 200-review evaluation sample matching Sprint 2's Transformer test). Also loaded pretrained GloVe word embeddings (50-dim) to demonstrate semantic similarity via nearest neighbors and direct word-pair similarity scores. Compared TF-IDF+LogReg (91.5% accuracy) against Sprint 2's pretrained DistilBERT Transformer (86.0% accuracy) on the same 200 reviews, concluding TF-IDF was the stronger, simpler representation for this particular sentiment task despite not capturing semantic meaning directly.
- **`03_C.-Vis. Preprocessing_OpenCV.ipynb` — Image Preprocessing:** Loaded the waste-classification bag images (garbage/paper/plastic) with OpenCV, compared Matplotlib (RGB) vs. cv2 (BGR) loading and converted between color spaces, inspected individual RGB channels, converted to grayscale, practiced resizing/scaling (including interpolation for upscaling) and pixel normalization, applied convolution kernels for sharpening and blurring, then built two reusable functions: a general `preprocess_image()` (read → BGR-to-RGB → resize → normalize, for CNN input) and a `preprocess_for_mobilenet()` variant using MobileNetV2's own required preprocessing. Also built and visualized a Keras augmentation pipeline (random flip, rotation, zoom, brightness).

## Status
This sprint is still in progress — only 3 of an expected 5 daily notebooks are present, and there's no `plan.md` backlog file yet (unlike Sprints 1 and 2). This README will need updating once the remaining days and a sprint plan/closeout are added.
