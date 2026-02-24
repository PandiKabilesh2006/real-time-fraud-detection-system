from src.inference.predict import FraudModel
from src.features.build_features import build_features

model=FraudModel()
transaction={
    "amount":150.0,
    "time":45000
}
features=build_features(transaction)
score=model.predict(features)

print("Fraud probability:", score)