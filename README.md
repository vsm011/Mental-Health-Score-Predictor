# Mental Health Score Predictor

An end-to-end machine learning application that predicts students' mental health scores based on social media usage patterns and lifestyle habits, integrated with a **Mistral AI-powered chatbot** for conversational mental wellness support. The application uses a FastAPI backend, an interactive web frontend, and LangChain for LLM integration.

**[Live Demo](https://mental-health-score-predictor-2-sr9h.onrender.com)** | **[Live API](https://mental-health-score-predictor-1-jc6j.onrender.com/docs)** | **[GitHub Repository](https://github.com/vsm011/Mental-Health-Score-Predictor)** | **[Notebook](./mhsp.ipynb)**

---

## Overview

Excessive or poorly balanced social media use can influence student wellbeing. This project estimates a student's mental health score using social media usage behavior and lifestyle factors, then makes the prediction accessible through an interactive web application.

In addition to ML-based predictions, the application features an AI wellness chatbot powered by **Mistral AI and LangChain**. Users can discuss stress, sleep, studies, motivation, and general wellbeing. With explicit user consent, the chatbot can also receive the latest predicted score as additional conversation context.

The application combines machine learning, API development, frontend engineering, and generative AI into a single deployed solution.

## Features

### 1. Machine Learning-Based Prediction
- End-to-end ML pipeline: data preprocessing, model comparison, hyperparameter tuning, and evaluation.
- Random Forest Regressor for predicting mental health scores on a 0–10 scale.
- Input validation using Pydantic.
- Real-time predictions through a web interface.

### 2. AI Wellness Chatbot
- Mistral AI integration using LangChain.
- Conversational support for topics such as stress, anxiety, sleep, studies, and emotional wellbeing.
- Conversation history maintained across follow-up messages.
- Optional sharing of the latest predicted mental health score with the chatbot.
- Context-aware responses based on the assessment score when the user provides consent.
- Safety-oriented instructions to avoid clinical diagnoses and medication recommendations.

### 3. Full-Stack Application
- FastAPI backend exposing REST API endpoints.
- Interactive frontend built using HTML, CSS, and JavaScript.
- Separate prediction and chatbot API endpoints.
- CORS-enabled backend for frontend integration.
- Cloud deployment using Render.

## Dataset

- **Source:** Kaggle — [Student Social Media And Mental Health Impact](https://www.kaggle.com/datasets/shivasingh4945/student-social-media-and-mental-health-impact)
- **Target variable:** `Mental_Health_Score` — a continuous score on a 0–10 scale.
- **Features used:**
  - Age
  - Gender
  - Country
  - Academic Level
  - Most Used Platform
  - Purpose of Use
  - Average Daily Usage Hours
  - Daily Unlocks
  - Study Hours
  - Physical Activity Hours
  - Sleep Hours per Night
  - Stress Level

**Feature engineering note:** Countries were grouped into the most frequent countries in the dataset plus an "Other" category to reduce categorical cardinality before encoding.

## Modeling & Results

Three models were trained and compared:

| Model | R² | Training R² | MAE | RMSE |
|---|---:|---:|---:|---:|
| Linear Regression | 0.740 | 0.724 | 0.536 | 0.676 |
| Random Forest (Default) | 0.877 | 0.981 | 0.349 | 0.465 |
| **Random Forest (Tuned)** | **0.865** | **0.955** | **0.369** | **0.487** |

- **Final model:** Random Forest Regressor.
- **Hyperparameter tuning:** RandomizedSearchCV.
- **Test R²:** 0.865.
- **Test MAE:** 0.369.

**Model selection:** Although the default Random Forest achieved a slightly higher test R², the tuned model was selected for deployment because it demonstrated a smaller training-to-test performance gap, indicating comparatively better generalization.

## AI Chatbot Architecture

The chatbot uses LangChain to connect the application with the Mistral language model.

**Conversation flow:**

1. The user submits a message through the frontend.
2. The frontend sends the message and recent conversation history to the FastAPI `/chat` endpoint.
3. The chatbot service constructs a prompt using the system instructions, conversation history, and optional assessment context.
4. LangChain invokes the Mistral model.
5. The generated response is returned to the frontend and displayed in the chat interface.

**Assessment context sharing:**

Users can explicitly enable an option to share their latest predicted score with the chatbot. When enabled, the score is included in the chatbot request as supplementary context.

The chatbot follows predefined instructions to provide general wellness information, avoid diagnosing medical conditions, and encourage professional support when appropriate.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python, JavaScript |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Serialization | Joblib |
| Backend | FastAPI, Pydantic, Uvicorn |
| Generative AI | Mistral AI |
| LLM Framework | LangChain |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |
| Version Control | Git, GitHub |

## Project Structure

```text
Mental-Health-Score-Predictor/
│
├── chatbot/
│   ├── __init__.py
│   ├── llm.py                 # Mistral model configuration
│   ├── prompt.py              # Chatbot system prompt
│   └── chat_service.py        # Conversation and LLM logic
│
├── schemas/
│   ├── __init__.py
│   └── chat_schema.py         # Chat API request/response schemas
│
├── data/
│   └── Student Social Media And Mental Health Impact.csv
│
├── mhsp.ipynb                # EDA, preprocessing and model training
├── main.py                   # FastAPI application
├── Mental_Health_Model.pkl   # Trained Random Forest model
│
├── index.html                # Frontend interface
├── style.css                 # Frontend styling
├── script.js                 # Prediction and chatbot integration
│
├── .env.example              # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/vsm011/Mental-Health-Score-Predictor.git

cd Mental-Health-Score-Predictor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
MISTRAL_MODEL=mistral-small-latest
```

Obtain an API key from [Mistral AI](https://console.mistral.ai/).

**Important:** Never commit your actual `.env` file or API key to GitHub.

### 5. Run the FastAPI backend

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Run the frontend

Open `index.html` using a local development server such as VS Code Live Server.

Ensure that the frontend API configuration in `script.js` points to your local backend:

```javascript
const API_BASE = "http://127.0.0.1:8000";
const CHAT_API_BASE = API_BASE;
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API root |
| POST | `/predict` | Predicts the mental health score |
| POST | `/chat` | Generates an AI chatbot response |

Interactive documentation is available through the FastAPI Swagger UI at `/docs`.

### Example: Prediction API

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
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

### Example: Chatbot API

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d '{
  "message": "I have been feeling stressed about my studies. What should I do?",
  "chat_history": [],
  "assessment_context": null
}'
```

The chatbot returns a generated response in JSON format.

## Live Deployment

The application is deployed using two Render services:

| Component | Deployment |
|---|---|
| Frontend | [Mental Health Score Predictor](https://mental-health-score-predictor-2-sr9h.onrender.com) |
| Backend | [FastAPI Backend](https://mental-health-score-predictor-1-jc6j.onrender.com) |
| API Documentation | [Swagger UI](https://mental-health-score-predictor-1-jc6j.onrender.com/docs) |

The backend uses environment variables configured through the Render dashboard to securely access the Mistral API.

**Note:** Render's free-tier services may spin down after inactivity. The first request after a period of inactivity can take longer while the service wakes up.

## Limitations & Future Work

- The model is trained on self-reported survey data, which may contain response bias.
- The predicted score is an ML-generated estimate, not a clinical assessment or diagnosis.
- Chatbot responses are generated by an LLM and may not always be accurate.
- Conversation history is maintained on the frontend and is not persisted across page refreshes.
- Model performance could be improved through additional feature engineering, ensembling, or gradient-boosted models such as XGBoost and LightGBM.
- Future improvements could include persistent conversation storage, user authentication, improved evaluation of chatbot responses, and more robust safety mechanisms.

## Disclaimer

This application is intended for educational and informational purposes. The predicted mental health score is not a clinical diagnosis or a substitute for professional mental healthcare. The AI chatbot provides general wellness information and should not be used for emergency or clinical decision-making.

---

**Developed as an end-to-end machine learning and generative AI project.**