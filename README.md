# Mental Health Score Predictor

A full-stack machine learning application that predicts a student's mental health score from social media usage patterns and lifestyle habits, served through a FastAPI backend with a web-based frontend for real-time predictions.

**[Live Demo](https://mental-health-score-predictor-2-sr9h.onrender.com)** &nbsp;|&nbsp; **[Live API](https://mental-health-score-predictor-1-jc6j.onrender.com/docs)** &nbsp;|&nbsp; **[Notebook](./mhsp.ipynb)** &nbsp;|&nbsp; **[API Source](./main.py)**

---

## Overview

Excessive or poorly balanced social media use is increasingly linked to student wellbeing outcomes. This project builds a regression model that estimates a student's mental health score from usage behavior (daily screen time, phone unlocks, platform, purpose of use) alongside lifestyle factors (sleep, study hours, physical activity, stress level), then exposes the model as a REST API with a simple web UI for interactive predictions.

## Features

- End-to-end ML pipeline: data preprocessing → model comparison → hyperparameter tuning → deployment
- REST API (FastAPI) with input validation via Pydantic
- Interactive web frontend (HTML/CSS/JS) for real-time score prediction
- CORS-enabled API, ready to be consumed by any frontend/client

## Dataset

- **Source:** Kaggle — [*"Student Social Media And Mental Health Impact"*](https://www.kaggle.com/datasets/shivasingh4945/student-social-media-and-mental-health-impact) dataset
- **Target variable:** `Mental_Health_Score` — a continuous score on a 0–10 scale
- **Features used:** Age, Gender, Country, Academic Level, Most Used Platform, Purpose of Use, Avg Daily Usage Hours, Daily Unlocks, Study Hours, Physical Activity Hours, Sleep Hours per Night, Stress Level

**Feature engineering note:** Countries were grouped into the top 10 most frequent countries in the dataset (India, USA, Canada, Australia, UK, Germany, Mexico, Turkey, France) plus an "Other" bucket, to reduce cardinality in the categorical feature before encoding.

## Modeling & Results

Three models were trained and compared:

| Model | R² | Training R² | MAE | RMSE |
|---|---|---|---|---|
| Linear Regression | 0.740 | 0.724 | 0.536 | 0.676 |
| Random Forest (default) | 0.877 | 0.981 | 0.349 | 0.465 |
| **Random Forest (tuned)** | 0.865 | 0.955 | 0.369 | 0.487 |

- **Final model:** Random Forest Regressor, hyperparameter-tuned via `RandomizedSearchCV`
- **Test R²:** 0.865 (86.5%) &nbsp;|&nbsp; **MAE:** 0.369

**Note on model selection:** the default Random Forest actually scored marginally higher on the test set (R² 0.877) than the tuned version (R² 0.865). The default model's much larger gap between training R² (0.981) and test R² (0.877) suggests more overfitting, however, so the tuned model — with a smaller train/test gap (0.955 vs. 0.865) — was selected as the better-generalizing option for deployment, at a small cost in raw test R².

## Tech Stack

- **Modeling:** Python, scikit-learn, Pandas, NumPy
- **API:** FastAPI, Pydantic, Uvicorn
- **Model serialization:** joblib
- **Frontend:** HTML, CSS, JavaScript

## Project Structure

```
Mental-Health-Score-Predictor/
├── data/                     # Dataset
├── mhsp.ipynb                # EDA, preprocessing, model training & comparison
├── main.py                   # FastAPI backend serving the trained model
├── Mental_Health_Model.pkl   # Serialized tuned Random Forest model
├── index.html                # Frontend UI
├── script.js                 # Frontend logic (calls the API)
├── style.css                 # Frontend styling
└── requirements.txt          # Python dependencies
```

## Setup & Usage

### 1. Clone the repo
```bash
git clone https://github.com/vsm011/Mental-Health-Score-Predictor.git
cd Mental-Health-Score-Predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

### 4. Use the frontend
Open `index.html` in a browser (with the API running) to get predictions through the UI.

### Live Deployment
Both services are deployed on [Render](https://render.com):
- **Frontend:** https://mental-health-score-predictor-2-sr9h.onrender.com
- **Backend API:** https://mental-health-score-predictor-1-jc6j.onrender.com (interactive docs at `/docs`)

> Note: Render's free tier spins services down after inactivity, so the first request after a period of idle time may take up to a minute (cold start) while the instance wakes up.

### Example API request
```bash
curl -X POST "https://mental-health-score-predictor-1-jc6j.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 21,
    "gender": "Male",
    "country": "India",
    "academic_level": "Undergraduate",
    "most_used_platform": "Instagram",
    "purpose_of_use": "Entertainment",
    "avg_daily_usage_hours": 4.5,
    "daily_unlocks": 60,
    "study_hours": 3,
    "physical_activity_hours": 1,
    "sleep_hours_per_night": 6.5,
    "stress_level": "High"
  }'
```

## Limitations & Future Work

- Trained on self-reported survey data, which can carry response bias
- Model performance could be pushed further with additional feature engineering, ensembling, or gradient-boosted models (XGBoost/LightGBM)
- No live-hosted deployment yet (API is local-only); could be containerized (Docker) and deployed to a cloud service for a public demo link
