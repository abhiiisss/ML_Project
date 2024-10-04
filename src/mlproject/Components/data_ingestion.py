import os 
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    test_data_path:str = os.path.join('artifacts', 'test_data.csv')
    train_data_path:str = os.path.join('artifacts', 'train_data.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')


class DataIngestion:
    def __init__(self):
        self.injestionConfig = DataIngestionConfig()

    def intiate_data_injestion(self):

        try:
            #reading the data from sql
            df = read_sql_data()
            logging.info("Completed Reading MySql Database")

            os.makedirs(os.path.dirname(self.injestionConfig.train_data_path), exist_ok= True)

            df.to_csv(self.injestionConfig.raw_data_path, index= False, header= True)

            train_set, test_set = train_test_split(df, test_size = 0.2, random_state= 42)
            train_set.to_csv(self.injestionConfig.train_data_path,index= False, header= True)
            test_set.to_csv(self.injestionConfig.test_data_path,index= False, header= True)

            logging.info("Data Injestion is Completed")

            return(

                self.injestionConfig.train_data_path,
                self.injestionConfig.test_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)
