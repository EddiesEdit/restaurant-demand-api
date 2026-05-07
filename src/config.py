from pathlib import Path

# =========================
# PATHS
# =========================
print("Laading Our Paths")

DATA_PATH = Path("data/raw/food_sales_raw.csv")

PROCESSED_DATA_PATH = Path("data/processed/processed_data.csv")

MODEL_PATH = Path("models/pipeline.pkl")

ARTIFACTS_DIR = Path("artifacts")

METRICS_PATH = ARTIFACTS_DIR / "metrics.json"

PREDICTIONS_PATH = ARTIFACTS_DIR / "predictions.csv"

print("Successfully Configured our Paths")