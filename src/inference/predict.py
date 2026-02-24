import joblib
import numpy as np

MODEL_PATH="models/fraud_model.pkl"

class FraudModel:
    def __init__(self):
        self.model=joblib.load(MODEL_PATH)
    
    def predict(self,features:list)->float:
        features_array=np.array(features).reshape(1,-1)
        fraud_probability=self.model.predict_proba(features_array)[0][1]
        return fraud_probability