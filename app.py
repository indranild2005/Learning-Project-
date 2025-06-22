import os
import sys
sys.path.append(os.path.join(os.getcwd(), "src"))
from LearningProject.logger import logging
from LearningProject.exception import CustomException
from LearningProject.components.data_ingestion import DataIngestion
from LearningProject.components.data_ingestion import DataIngestionConfig


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
        

  
