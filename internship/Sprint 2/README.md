# Sprint 2 — Deep Learning: CNNs, RNNs/LSTM & Transformers

Sprint 2 of the Phase 3 capstone: survey the main deep-learning architectures (CNN, RNN/LSTM, Transformer) hands-on, decide which fits the project's data, and ship a tuned final model. The sprint plan originally targeted image waste classification, but after the CNN experiments (Days 1–2) the project's actual dataset turned out to be sequential ECG signal data, so the sprint pivoted to a tuned LSTM as the final core model (see "Note on scope" below).

## Contents

```
Sprint 2/
├── plan.md                        <- sprint goal, backlog, acceptance criteria (image-classification framing)
└── notebooks/
    ├── 01_CNN_fundamentals.ipynb  <- Day 1: manual convolution, edge-detection filter, parameter sharing
    ├── 02_CNN.ipynb               <- Day 2: CNN from scratch, data augmentation, transfer learning (MobileNetV2)
    ├── 03_RNN_LSTM.ipynb          <- Day 3: SimpleRNN vs. LSTM on ECG sequence data, mentor-review prep
    ├── 04_Transormers.ipynb       <- Day 4: pretrained DistilBERT transformer on IMDb sentiment, vs. Day 3 LSTM
    └── 05_Closeout.ipynb          <- Day 5: tuned final LSTM, metric comparison, sprint retrospective
```

## Day-by-day summary

- **Day 1 — CNN Fundamentals (`01_CNN_fundamentals.ipynb`):** Loaded an image dataset (waste categories: plastic/paper/garbage bags), inspected class distribution and sample images, manually applied a 3x3 vertical edge-detection kernel to one grayscale image and visualized the resulting feature map, and computed how many fewer parameters a convolution filter uses versus an equivalent dense layer — motivating CNN as the initial candidate architecture.
- **Day 2 — CNN & Transfer Learning (`02_CNN.ipynb`):** Split the image dataset into train/validation, built and trained a CNN from scratch (overfit: ~99.3% train vs. ~91% val accuracy), added data augmentation (random flip/rotation/zoom) to close the gap (~96.5% train vs. ~94.8% val), then applied transfer learning with a frozen MobileNetV2 backbone, which won on every metric (~99.8% train / ~97.3% val accuracy, lowest val loss).
- **Day 3 — RNN & LSTM (`03_RNN_LSTM.ipynb`):** Switched to the MIT-BIH ECG heartbeat dataset (5-class, sequential, imbalanced), reshaped it for Keras' (samples, timesteps, features) format, computed balanced class weights, and compared a SimpleRNN against an LSTM over 10 epochs — the LSTM clearly outperformed (macro F1 higher) — with an explanation of why order-awareness matters for ECG signals.
- **Day 4 — Transformers (`04_Transormers.ipynb`):** Loaded a pretrained DistilBERT sentiment model (Hugging Face) on the IMDb reviews dataset, ran it on a single review and then a 200-review sample, evaluated accuracy/classification report/confusion matrix, explained attention vs. RNN/LSTM sequential memory, and concluded Transformers weren't selected as the ECG project's core architecture since DistilBERT is designed for text, not numerical time-series.
- **Day 5 — Close-Out (`05_Closeout.ipynb`):** Returned to the ECG/LSTM task from Day 3, built a tuned LSTM (128 units, dropout, small learning rate, EarlyStopping) with manually softened class weights (found to work better than automatically balanced weights, which over-corrected and over-predicted rare classes), reaching ~92.7% test accuracy, macro precision 0.711, macro recall 0.643, macro F1 0.671 — selected as the final Sprint 2 core model.

## Key results

**CNN experiments (Day 2, waste images):**

| Model | Train Acc. | Val Acc. | Train Loss | Val Loss | Observation |
|---|---:|---:|---:|---:|---|
| Basic CNN | 0.993 | 0.910 | 0.019 | 0.539 | Clear overfitting |
| CNN + Augmentation | 0.965 | 0.948 | 0.096 | 0.190 | Better generalization |
| MobileNetV2 Transfer Learning | **0.998** | **0.973** | **0.012** | **0.077** | Best validation performance |

**Final sequence model (Day 5, ECG heartbeat, tuned LSTM):** ~92.7% test accuracy, macro precision 0.711, macro recall 0.643, macro F1 0.671 — the selected Sprint 2 core model.

## Note on scope
`plan.md` frames Sprint 2 around image waste classification, and Days 1–2 follow that plan closely (including a full CNN vs. transfer-learning comparison). From Day 3 onward the work shifts to the ECG heartbeat dataset used in Sprint 1, and the sprint's final model selection (Day 5) is the tuned LSTM rather than a CNN — the plan document has not been updated to reflect this pivot.
