from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

def train_model(df):
    X = df[['Account_Age_Days','Login_Frequency','Daily_Usage_Mins']]
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred)
    }

    return model, metrics


def predict_churn(df, model):
    X = df[['Account_Age_Days','Login_Frequency','Daily_Usage_Mins']]
    df['Churn_Prediction'] = model.predict(X)

    df['Risk_Level'] = df['Churn_Prediction'].map({
        1: 'High Risk',
        0: 'Safe'
    })

    return df