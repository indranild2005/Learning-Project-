import os
import sys
sys.path.append(os.path.join(os.getcwd(), "src"))
from LearningProject.logger import logging
from LearningProject.exception import CustomException
import pandas as pd 
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql


import pickle
import numpy as np

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        if not all([host, user, password, db]):
            raise CustomException("Database credentials are not set properly in the .env file.", sys)

        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established")

        df = pd.read_sql_query('SELECT * FROM students', mydb)
        mydb.close()

        print(df.head())
        return df

    except Exception as ex:
        raise CustomException(ex, sys)

    