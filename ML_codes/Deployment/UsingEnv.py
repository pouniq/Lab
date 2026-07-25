
import os
from dotenv import load_dotenv
import pandas as pd

# load values from .env files
load_dotenv()

dataset_path = os.getenv("DATASET_PATH")
model_path = os.getenv("MODEL_PATH")
enviroment = os.getenv("ENVIROMENT")
target_col = os.getenv("TARGET_COL")

df = pd.read_csv(dataset_path)
df[target_col].value_counts()

X = df.drop(columns = [target_col])
y = df[target_col]

## secret informations should NOT be hard coded into your 
## python script but you should put it inside your .env file
## or saving configurable values.

