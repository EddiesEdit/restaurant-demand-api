# Restaurant Demand API

A production-ready machine learning API for forecasting restaurant food demand using time-series and contextual sales data. This project combines feature engineering, scalable preprocessing pipelines, and FastAPI deployment to predict restaurant dish sales efficiently.

---

# Project Overview

Restaurant food demand fluctuates due to multiple factors such as:

- Seasonal trends
- Weekends and working days
- Pricing variations
- Dish popularity
- Holidays and festivals
- Restaurant locality
- Meal characteristics

This project uses machine learning to model these patterns and predict the number of units sold for different dishes across restaurant locations.

The goal is to build a complete end-to-end ML system:
- Data preprocessing
- Feature engineering
- Model training
- Evaluation
- Pipeline serialization
- API deployment with FastAPI

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Uvicorn
- Joblib

---

# Project Structure

```bash
ml_project/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── model_loader.py
│   ├── predictor.py
│
├── models/
│   └── pipeline.pkl
│
├── notebooks/
│   └── experiments.ipynb
│
├── src/
│   ├── pipeline.py
│   ├── train.py
│   ├── evaluate.py
│   ├── config.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── artifacts/
│
├── requirements.txt
├── README.md
├── .gitignore
└── run.py