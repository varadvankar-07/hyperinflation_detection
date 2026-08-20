# Hyperinflation Event Detection

An end-to-end machine learning pipeline to detect and classify hyperinflation
events using IMF World Economic Outlook (WEO) data, covering ~195 countries
from 1980–2024.

## Table of Contents
- [Overview](#overview)
- [Motivation](#motivation)
- [Data](#data)
- [Project Structure](#project-structure)
- [Pipeline](#pipeline)
- [Handling Class Imbalance](#handling-class-imbalance)
- [Preventing Data Leakage](#preventing-data-leakage)
- [Results](#results)
- [Setup](#setup)
- [Usage](#usage)
- [Limitations & Future Work](#limitations--future-work)
- [License](#license)

## Overview
This project frames hyperinflation detection as a **binary classification**
problem: given a country's macroeconomic indicators up to a given year,
predict whether it will experience a hyperinflation event (defined here as
annual inflation exceeding 50%) in that year.

The pipeline covers the full workflow — raw data cleaning, feature
engineering from time series, a chronological train/test split, and a
gradient-boosted model trained to handle severe class imbalance.

## Motivation
Hyperinflation events are rare, disruptive, and historically hard to predict
using headline indicators alone. This project explores whether structured
lag- and trend-based features derived from a country's own inflation history
can give useful early signal, using publicly available IMF data rather than
proprietary economic indicators.

## Data
- **Source:** [IMF World Economic Outlook (WEO) database](https://www.imf.org/en/Publications/WEO)
- **Coverage:** ~195 countries, 1980–2024
- **Target definition:** A country-year is labeled positive if annual
  inflation exceeds 50%
- **Class distribution:** ~3.5% positive (hyperinflation) events — a
  significantly imbalanced dataset
- Raw data is provided in wide format (years as columns) and reshaped to
  long format for time-series feature engineering

> **Note:** Raw IMF data files are not included in this repo (see
> `.gitignore`). See [Setup](#setup) for how to obtain them.

## Project Structure
```
hyperinflation-detection/
├── data/                  # (gitignored) raw and processed data
├── notebooks/             # exploratory analysis, EDA
├── src/                   # pipeline scripts (cleaning, features, model)
├── requirements.txt
├── README.md
└── .gitignore
```

## Pipeline

**1. Data Cleaning**
- Reshaped raw wide-format WEO data (years as columns) into long format
  using `pd.melt`, producing one row per country-year
- Handled missing values via row-level dropping after feature construction

**2. Feature Engineering**
- **Lag features:** inflation values at *t-1*, *t-2*, *t-3*
- **Rolling statistics:** rolling mean and standard deviation over 3-year
  and 5-year windows
- **Acceleration:** year-over-year change in inflation rate
- **High-inflation frequency:** count of high-inflation years within a
  rolling 5-year window
- All rolling/lag transforms applied with `.shift()` **before** computing
  statistics, to avoid leaking future information into past rows

**3. Train/Test Split**
- Chronological split at **2015** (train: pre-2015, test: 2015 onward)
- No random shuffling — time-ordered splits are essential for time series
  problems to avoid leakage from future to past

**4. Model**
- **XGBoost** classifier as baseline
- `scale_pos_weight` set to counteract the ~3.5% positive class rate,
  penalizing misclassification of the minority (hyperinflation) class more heavily

## Handling Class Imbalance
With only ~3.5% of country-years labeled as hyperinflation events, naive
accuracy is a poor metric — a model predicting "no hyperinflation" for every
row would already score ~96.5%. This project addresses that through:
- `scale_pos_weight` in XGBoost, which up-weights the minority class during
  training
- Evaluation on precision, recall, and F1 rather than accuracy alone
  (see [Results](#results))

## Preventing Data Leakage
Two safeguards were used throughout:
1. **`.shift()` before rolling calculations** — ensures rolling
   mean/std/lag features for year *t* only use information available up to
   *t-1*, never *t* itself.
2. **Chronological (not random) train/test split** — ensures the model is
   never trained on data from years after its test period, which would
   otherwise leak future economic conditions into training.

## Results

| Metric | Score |
|---|---|
| Precision | 0.62 |
| Recall |0.84 |
| F1-score | 0.71 |

## Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| 0 | 1.00 | 0.99 | 0.99 | 1886 |
| 1 | 0.62 | 0.84 | 0.71 | 38 |
| **Accuracy** | | | **0.99** | **1924** |
| **Macro Avg** | **0.81** | **0.92** | **0.85** | **1924** |
| **Weighted Avg** | **0.99** | **0.99** | **0.99** | **1924** |

## Confusion Matrix

| | Predicted 0 | Predicted 1 |
|---|---:|---:|
| **Actual 0** | 1866 | 20 |
| **Actual 1** | 6 | 32 |

## Setup
```bash
# Clone the repo
git clone <your-repo-url>
cd hyperinflation-detection

# Install dependencies
pip install -r requirements.txt
```
Data setup: download the IMF WEO dataset from the link above and place it
in `imf.org/`


## Limitations & Future Work
- Baseline model only — no hyperparameter tuning performed yet
- Feature set is derived solely from inflation history; incorporating other
  macroeconomic indicators (money supply growth, exchange rate volatility,
  fiscal deficit) could improve signal
- Class imbalance handled via `scale_pos_weight` only — SMOTE or other
  resampling techniques not yet explored
- No cross-validation across multiple chronological splits yet (single
  2015 cutoff)
