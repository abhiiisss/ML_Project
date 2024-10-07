from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.Components.data_ingestion import DataIngestion
from src.mlproject.Components.data_transformation import DataTransformation, DataTransformationConfig
from src.mlproject.Components.model_training import ModelTrainer, ModelTrainerConfig
import sys

if __name__ == "__main__":
    logging.info("The execution has started")


try:
    data_injestion = DataIngestion()
    train_data_path, test_data_path = data_injestion.intiate_data_injestion()


    data_transformation=DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_trasformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))

except Exception as e:
    logging.info("Exception has been raised")
    raise CustomException(e, sys)
