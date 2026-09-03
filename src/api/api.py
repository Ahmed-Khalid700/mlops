import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.utils.helper import model_path, model_columns

app = FastAPI(title="Driver Active Status Prediction API")


model = joblib.load(model_path)
model_columns = joblib.load(model_columns)


class DriverInput(BaseModel):
    Age: int
    City: str
    Experience_Years: int
    Average_Rating: float


@app.get("/")
def root():
    return {"message": "Driver Active Status API is running"}


@app.post("/predict")
def predict(data: DriverInput):
    input_df = pd.DataFrame([data.model_dump()])

    input_df = pd.get_dummies(input_df, columns=["City"], drop_first=True, dtype=int)

    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0].tolist()

    return {
        "prediction": int(prediction),
        "status": "Active" if prediction == 1 else "Inactive",
        "probabilities": {
            "Inactive": probability[0],
            "Active": probability[1],
        },
    }
