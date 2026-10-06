from sklearn.metrics import confusion_matrix
import joblib
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
import pandas as pd
from feature_extraction import extract_features
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("dataset/raw/urls.csv", sep="\t")

print(df.head())
print(df.shape)
print(df.columns)
print(df['label'].value_counts())
print(df.isnull().sum())
df = df.dropna(subset=['url'])
df = df.drop_duplicates(subset=['url'])
df = df[df['label'].isin([0, 1])]
print(df.shape)


feature_rows = []

for url in df["url"]:
    feature_rows.append(extract_features(url))

features_df = pd.DataFrame(feature_rows)
features_df["label"] = df["label"].values

features_df.to_csv(
    "dataset/processed/features.csv",
    index=False
)

X = features_df.drop("label", axis=1)

y = features_df["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


lr = LogisticRegression(
    max_iter=1000
)

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)


dt = DecisionTreeClassifier(
    max_depth=15,
    random_state=42
)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)


def evaluate_model(name, y_test, prediction):

    print(name)

    print(
        "Accuracy:",
        accuracy_score(y_test, prediction)
    )

    print(
        "Precision:",
        precision_score(y_test, prediction)
    )

    print(
        "Recall:",
        recall_score(y_test, prediction)
    )

    print(
        "F1:",
        f1_score(y_test, prediction)
    )

    print(
        classification_report(
            y_test,
            prediction
        )
    )


evaluate_model(
    "Logistic Regression",
    y_test,
    lr_pred
)

evaluate_model(
    "Decision Tree",
    y_test,
    dt_pred
)

evaluate_model(
    "Random Forest",
    y_test,
    rf_pred
)


cm = confusion_matrix(
    y_test,
    rf_pred
)

print(cm)


joblib.dump(
    rf,
    "model/random_forest.pkl"
)
