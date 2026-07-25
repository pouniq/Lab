import os
import logging
from dotenv import load_dotenv
import pandas as pd


# load .evn content to env variables
load_dotenv()

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers= [
        logging.StreamHandler(), # terminal
        logging.FileHandler("app.log")    # file
        
    ]
)
logging.info("program started")
logging.debug("debugging code")
logging.warning("this is a WARNING message")
logging.error("this is a ERROR message")


DATASET_PATH = os.getenv("DATASET_PATH")
logging.info('loading dataset')
df = pd.read_csv(DATASET_PATH)
logging.info('dataset loaded successfully')
print(df.head())



MODEL_PATH = os.getenv("MODEL_PATH")

