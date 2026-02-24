def build_features(transaction: dict) -> list:
    """
    Build a 30-feature input vector that matches the model's training schema.

    Expected order:
    [Time, V1, V2, ..., V28, Amount]
    """

    time = transaction["time"]
    amount = transaction["amount"]

    # Since V1–V28 are anonymized features and
    # not available in real-time demo input,
    # we initialize them to 0.0
    v_features = [0.0] * 28

    features = [time] + v_features + [amount]

    return features
