import joblib
from feature_extraction import extract_features

model = joblib.load(
    "model/random_forest.pkl"
)

print("Model classes:", model.classes_)


def predict_url(url):

    features = extract_features(url)

    feature_values = [
        list(features.values())
    ]

    print("\n==============================")
    print("URL:", url)
    print("Features:", features)
    print("Feature Values:", feature_values)

    prediction = model.predict(
        feature_values
    )[0]

    probabilities = model.predict_proba(
        feature_values
    )[0]

    print("Prediction:", prediction)
    print("Probability:", probabilities)

    confidence = max(probabilities)

    if prediction == 0:
        result = "Phishing"
    else:
        result = "Legitimate"

    print("Final Result:", result)
    print("Confidence:", confidence)
    print("==============================\n")

    return result, confidence, features
