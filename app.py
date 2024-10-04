from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.Components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("The execution has started")


try:
    data_injestion = DataIngestion()
    data_injestion.intiate_data_injestion()

except Exception as e:
    logging.info("Exception has been raised")
    raise CustomException(e, sys)
