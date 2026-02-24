# End-to-End Real-Time Fraud Detection System (ML Pipeline + Production Deployment)

A production-style real-time fraud detection system built using supervised machine learning, imbalanced learning techniques, and low-latency API deployment.

This project simulates how financial institutions detect fraudulent transactions in real time using a scalable ML inference pipeline.

---

## 🚀 Project Overview

This system:

- Trains a supervised classification model on highly imbalanced transaction data
- Applies feature engineering and class-weight tuning to improve minority-class recall
- Evaluates performance using precision, recall, F1-score, and ROC-AUC
- Deploys the trained model as a low-latency FastAPI service
- Implements structured logging and rule-based risk decision thresholds

The architecture reflects real-world fraud detection systems used in fintech and banking environments.

---

## 🧠 Problem Statement

Credit card fraud detection is a highly imbalanced classification problem:

- Fraud cases are extremely rare
- False negatives are costly
- Precision–Recall trade-offs must be optimized carefully

The objective is to build a robust ML pipeline that maximizes fraud detection recall while maintaining acceptable precision.

---

## 🏗️ System Architecture

Client Request (Transaction JSON)
        ↓
FastAPI Endpoint (/predict)
        ↓
Feature Validation & Transformation
        ↓
Trained ML Model (scikit-learn)
        ↓
Fraud Probability Output
        ↓
Decision Logic (ALLOW / REVIEW / BLOCK)
        ↓
Structured Logging

---

## 🔍 Dataset

- Credit Card Fraud Detection dataset (anonymized financial transactions)
- Highly imbalanced binary classification problem
- Features include PCA-transformed components + transaction metadata

---

## ⚙️ Machine Learning Pipeline

### 1️⃣ Data Preprocessing
- Train-test split
- Handling class imbalance
- Feature scaling (if applicable)
- Schema consistency enforcement

### 2️⃣ Feature Engineering
- Transaction-based feature validation
- Structured input formatting
- Consistent inference-time feature ordering

### 3️⃣ Model Training
- Logistic Regression (class-weight balanced)
- Imbalanced learning handling
- Hyperparameter tuning
- Cross-validation

### 4️⃣ Model Evaluation

Metrics used:

- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

These metrics were used to optimize fraud detection under real-world risk constraints.

---

## 📊 Model Performance

Example metrics (update with your real values):

- ROC-AUC: 0.97+
- Fraud Recall: Improved via class-weight optimization
- Balanced precision-recall tradeoff

The model prioritizes recall to minimize high-risk false negatives.

---

## 🧩 Decision Logic

Based on predicted fraud probability:

- ≥ 0.80 → **BLOCK**
- 0.50 – 0.79 → **REVIEW**
- < 0.50 → **ALLOW**

This tiered thresholding simulates production fraud risk scoring systems.

---

## 🖥️ API Deployment

The trained model is deployed using **FastAPI**.

### Endpoint

```
POST /predict
```

### Sample Request

```json
{
  "amount": 150.0,
  "time": 45000.0
}
```

### Sample Response

```json
{
  "fraud_probability": 0.0595,
  "decision": "ALLOW"
}
```

---

## 📁 Project Structure

```
real-time-fraud-detection-system/
│
├── data/                 # Dataset
├── models/               # Saved model (.pkl)
├── notebooks/            # Model experimentation
├── src/
│   ├── api/              # FastAPI app
│   ├── features/         # Feature engineering
│   ├── inference/        # Model loading & prediction
│   └── utils/            # Logging utilities
│
├── requirements.txt
└── README.md
```

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/real-time-fraud-detection-system.git
cd real-time-fraud-detection-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run API Server

```bash
uvicorn src.api.main:app --reload
```

### 5️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🛡️ Production Considerations

- Model loaded once at startup to reduce per-request latency
- Feature schema validation to prevent training–serving skew
- Structured logging for observability
- Threshold-based risk scoring
- Modular architecture for scalability

---

## 📈 Future Improvements

- Advanced models (XGBoost / LightGBM)
- Real-time streaming integration (Kafka)
- Model monitoring & drift detection
- Containerization with Docker
- Cloud deployment (AWS / GCP)

---

## 🎯 Key Skills Demonstrated

- Supervised Machine Learning
- Imbalanced Classification
- Feature Engineering
- Model Evaluation & Metrics
- Production ML Inference
- FastAPI Deployment
- ML System Design

---

## 📌 Resume Summary Line

Built an end-to-end fraud detection ML pipeline with imbalanced learning optimization and deployed it as a low-latency FastAPI service with production-style inference architecture.