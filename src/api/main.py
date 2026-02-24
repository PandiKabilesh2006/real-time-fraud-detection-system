from fastapi import FastAPI
from pydantic import BaseModel

from src.inference.predict import FraudModel
from src.features.build_features import build_features
from src.utils.logger import get_logger

app=FastAPI(title="Real-Time Fraud Detection API")
model=FraudModel()
logger=get_logger("fraud-api")

class TransactionRequest(BaseModel):
    amount:float
    time:float

@app.post("/predict")
def predict_fraud(transaction:TransactionRequest):
    transaction_dict=transaction.dict()
    logger.info(f"Received transaction: {transaction_dict}")

    features=build_features(transaction_dict)
    fraud_probability=model.predict(features)

    if(fraud_probability>=0.8):
        decision="BLOCK"
    elif(fraud_probability>=0.5):
        decision="REVIEW"
    else:
        decision="ALLOW"
    
    logger.info(
        f"Prediction: prob={fraud_probability:.4f},decision={decision}"
    )
    return {
        "fraud_probability":fraud_probability,
        "decision":decision
    }