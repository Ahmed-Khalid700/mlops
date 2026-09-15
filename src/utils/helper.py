from dotenv import load_dotenv
import os

load_dotenv()

data_path = os.getenv("DATA_PATH")
model_path = os.getenv("MODEL_PATH")
model_columns = os.getenv("MODEL_COLUMNS")
mlflow_tracking_url = os.getenv("MLFLOW_TRACKING_URI")