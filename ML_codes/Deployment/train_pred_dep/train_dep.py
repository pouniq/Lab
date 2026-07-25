# once you finalize your model, you can use it as a script
import os
from pathlib import Path
from dotenv import load_dotenv
import logging
from joblib import dump

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def train_model():
    try:
        
        load_dotenv()
        
        PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT"))
        DATASET_PATH = PROJECT_ROOT / os.getenv("DATASET_NAME")
        MODEL_PATH = PROJECT_ROOT / os.getenv("MODEL_DIR") / os.getenv("MODEL_NAME")
        LOG_PATH = PROJECT_ROOT / os.getenv("LOG_DIR") / os.getenv("LOG_NAME")

        TARGET_COL = os.getenv("TARGET_COL")
        TEST_SIZE = float(os.getenv("TEST_SIZE"))
        RANDOM_STATE = int(os.getenv("RANDOM_STATE"))

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler(),  # terminal
                logging.FileHandler("app.log")  # file
            ],
        )
        
        
        logging.info('Training section is started')
        df = pd.read_csv(DATASET_PATH)
        logging.info(f'dataframe is now in place with shape of {df.shape}')
        
        X = df.drop(columns=TARGET_COL)
        y = df[TARGET_COL]
        
        logging.info('X and y are now separated')
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=RANDOM_STATE, test_size=TEST_SIZE, stratify=y)
        logging.info('Train Test split is done.')
        
        pip = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(class_weight="balanced"))
            ]
        ) 
        pip.fit(X_train, y_train)
        logging.info('Model Training Completed')
        
        
        train_acc = accuracy_score(y_train, pip.predict(X_train))
        test_acc = accuracy_score(y_test, pip.predict(X_test))
        
        train_report = classification_report(y_train, pip.predict(X_train))
        test_report = classification_report(y_test, pip.predict(X_test))

        
        logging.info(f'train prediction accuracy {train_acc}')
        logging.info(f'test prediction accuracy {test_acc}')
        
        logging.info(f'train prediction report {train_report}')
        logging.info(f"test prediction report {test_acc}")
        
        dump(pip, MODEL_PATH)
        logging.info(f'model moved to {MODEL_PATH}')
        logging.info('Training Script finished.')
        
        
    except Exception as e:
        print(f"training failed: {e}")
        logging.exception(f"training script failed: {e}")
        raise


if __name__ == "__main__":
    train_model()
