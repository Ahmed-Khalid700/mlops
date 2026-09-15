import os
import joblib
import mlflow
import pandas as pd
from src.utils.helper import *
from sklearn.ensemble import RandomForestClassifier


mlflow.set_tracking_uri(mlflow_tracking_url)

mlflow.set_experiment("MLOPS TEST")

data = pd.read_csv(data_path)

y = data["Active_Status"]
x = data.drop(columns=["Active_Status", "Driver_ID", "Name"])
x = pd.get_dummies(x, columns=["City"], drop_first=True, dtype=int)

model = RandomForestClassifier(random_state=42)

with mlflow.start_run("Random Forset"):
    model.fit(x, y)

    mlflow.log_param("random_state", 42)

    mlflow.sklearn.log_model("model", model)

joblib.dump(model, model_path)
joblib.dump(x.columns.tolist(), model_columns)
print("Saved model and features schema successfully!")
