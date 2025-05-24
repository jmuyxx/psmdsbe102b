# psmdsbe102/config.py

from pathlib import Path
import mlflow

# Set up MLflow tracking
MODEL_REGISTRY = Path("/tmp/mlflow")
MODEL_REGISTRY.mkdir(parents=True, exist_ok=True)
MLFLOW_TRACKING_URI = "file://" + str(MODEL_REGISTRY.absolute())
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# Shared constants
DEFAULT_SEED = 42
DATA_PATH = "D:/PSM Data Science/2024-2025 Sem2/Advance Topics in Data Science/Hands-on Activity 3.1 Scripting & CLI/diabetes.csv"
