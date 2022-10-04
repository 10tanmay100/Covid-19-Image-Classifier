from covid_classifier.constants import *
from covid_classifier.utils import *
from covid_classifier.config import configuration
import os
from zipfile import ZipFile
from covid_classifier.entity import DataIngestionConfig
from covid_classifier import logger
from tqdm import tqdm
from pathlib import Path
import requests
import opendatasets as od

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        self.config=config
    def download_data(self):
        logger.info("Trying to download the file from direct kaggle")
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"{self.config.local_data_file} not exists, skipping")
            os.makedirs(self.config.local_data_file,exist_ok=True)
            logger.info(f"{self.config.local_data_file} created succesfully!!!")
            od.download(self.config.source_URL,data_dir=self.config.local_data_file)
            logger.info(f"file downloaded {self.config.local_data_file}")
        else:
            logger.info(f"{self.config.local_data_file} already exists")
            od.download(self.config.source_URL,data_dir=self.config.local_data_file)
            logger.info(f"Downloaded succesfully!!!! in the location {self.config.local_data_file}")
            
        
            
        
        



 