"""
Basic configuration and path
"""

from pathlib import Path

##Root Directory
BASE_DIR:Path = Path(__file__).resolve().parents[1]

##data and model path
DATA_DIR:Path= Path(BASE_DIR)/"data"
DATA_PATH:Path =Path(DATA_DIR)/"movie_metadata.csv"
CLEANED_DATA_Path:Path=Path(DATA_DIR)/"cleaned_data.csv"

MODEL_PATH:Path=Path(BASE_DIR)/"models"
BEST_MODEL_PATH:Path= Path(MODEL_PATH)/"best_model.joblib"
FEATURES_PATH:Path= Path(MODEL_PATH)/"feature_column.jason"

TARGET_COL:str ="imdb_score"

## Train,Test,CV
TEST_SIZE:float=0.2
RANDOM_STATE:int =42
CV_FOLDS:int=5
N_JOBS:int= -1
SCORING:str ="roc-auc"

print("The configurations are successfully applied")