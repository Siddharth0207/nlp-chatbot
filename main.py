import numpy as np
import pandas as pd
import sys
import os 
from src.chat_bot.logger import logging
from src.chat_bot.exception import CustomException




class LoadHuggingFaceDataSet:
    logging.info(f"Inside the Class for HuggingDataSet")

    def __init__(self, dataset_name:str, dataset_path:str):
        self.dataset_name = dataset_name
        self.data_path = dataset_path

    def load_data(self):
        logging.info(f"Loading dataset {self.dataset_name} from path {self.data_path}")
        try:
            import datasets
            dataset = datasets.load_dataset(self.dataset_name)
            return dataset
        except Exception as e:
            raise CustomException(e, sys)