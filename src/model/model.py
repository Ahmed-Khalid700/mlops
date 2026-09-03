import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src.utils.helper import model_path, model_columns, data_path

data = pd.read_csv(data_path)

y = data["Active_Status"]
x = data.drop(columns=["Active_Status", "Driver_ID", "Name"])
x = pd.get_dummies(x, columns=["City"], drop_first=True, dtype=int)

model = RandomForestClassifier(random_state=42)
model.fit(x, y)

joblib.dump(model, model_path)
joblib.dump(x.columns.tolist(), model_columns)
print("Saved model and features schema successfully!")
