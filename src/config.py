from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Main directories
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

REPORT_DIR = BASE_DIR / "reports"
MODEL_DIR = BASE_DIR / "models"


# Input and output files
RAW_FILE = RAW_DIR / "sales_raw.csv"

CLEAN_FILE = PROCESSED_DIR / "sales_cleaned.csv"

MODEL_FILE = MODEL_DIR / "sales_model.joblib"

METRICS_FILE = REPORT_DIR / "metrics.json"


# Random state
RANDOM_STATE = 42


# Create directories if they don't exist
for directory in [
    RAW_DIR,
    PROCESSED_DIR,
    REPORT_DIR,
    MODEL_DIR
]:
    directory.mkdir(
        parents=True,
        exist_ok=True
    )