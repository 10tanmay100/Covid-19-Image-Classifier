import os
from zipfile import ZipFile
from covid_classifier.config import configuration
from covid_classifier.entity import DataIngestionConfig
from covid_classifier.entity import DataValidationConfig
from covid_classifier import logger
from covid_classifier.utils import *
from covid_classifier.constants import *
from tqdm import tqdm
from pathlib import Path
import shutil
import requests

class DataValidation:
    def __init__(self,ingestion_config=DataIngestionConfig,validation_config=DataValidationConfig):
        self.ingestion_config=ingestion_config
        self.validation_config=validation_config
        self.config=read_yaml(CONFIG_FILE_PATH)
    
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if (f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"))]
    
    
    def check_data_gathering(self):
        logger.info("Checking data gathering......")
        if (len(os.listdir(self.ingestion_config.local_data_file+"/covid19-image-dataset/Covid19-dataset"))==self.config.validated_file.number_of_folders):
            if (len(os.listdir(self.ingestion_config.local_data_file_train))==self.config.validated_file.number_of_folders_train):
                if (len(os.listdir(self.ingestion_config.local_data_file_test))==self.config.validated_file.number_of_folders_test):
                    if (len(os.listdir(self.ingestion_config.local_data_file_train+"/Covid"))==self.config.validated_file.number_of_covid_files_train):
                        if (len(os.listdir(self.ingestion_config.local_data_file_train+"/Normal"))==self.config.validated_file.number_of_normal_files_train):
                            if (len(os.listdir(self.ingestion_config.local_data_file_train+"/Viral Pneumonia"))==self.config.validated_file.number_of_Viral_Pneumonia_files_train):
                                
                                if (len(os.listdir(self.ingestion_config.local_data_file_test+"/Covid"))==self.config.validated_file.number_of_covid_files_test):
                                    if (len(os.listdir(self.ingestion_config.local_data_file_test+"/Normal"))==self.config.validated_file.number_of_normal_files_test):
                                        if (len(os.listdir(self.ingestion_config.local_data_file_test+"/Viral Pneumonia"))==self.config.validated_file.number_of_Viral_Pneumonia_files_test):
                                            return True            
        return False
    
    def dump_clean_data(self):
        if self.check_data_gathering()==True:
            logger.info("Cleaning data and checking has been started!!!")
            os.makedirs(self.validation_config.validated_local_data_file,exist_ok=True)
            os.makedirs(self.validation_config.validated_local_data_file_train,exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_train}")
            os.makedirs(self.validation_config.validated_local_data_file_train+"/Covid",exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_train+'/Covid'}")
            os.makedirs(self.validation_config.validated_local_data_file_train+"/Normal",exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_train+'/Normal'}")
            os.makedirs(self.validation_config.validated_local_data_file_train+"/Viral Pneumonia",exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_train+'/Viral Pneumonia'}")
            os.makedirs(self.validation_config.validated_local_data_file_test,exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_test}")
            os.makedirs(self.validation_config.validated_local_data_file_test+"/Covid",exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_test+'/Covid'}")
            os.makedirs(self.validation_config.validated_local_data_file_test+"/Normal",exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_test+'/Normal'}")
            os.makedirs(self.validation_config.validated_local_data_file_test+"/Viral Pneumonia",exist_ok=True)
            logger.info(f"Directory created {self.validation_config.validated_local_data_file_test+'/Viral Pneumonia'}")
            logger.info("Cleaned photos sending to validated state directory")
            logger.info("Covid train data send is going on..")
            for photos in tqdm(self._get_updated_list_of_files(os.listdir(self.ingestion_config.local_data_file_train+"/Covid"))):
                if get_size(Path(self.ingestion_config.local_data_file_train+f"/Covid/{photos}"))>0:
                    shutil.copy(self.ingestion_config.local_data_file_train+f"/Covid/{photos}",self.validation_config.validated_local_data_file_train+"/Covid")
            
            logger.info("Normal train data send is going on..")
            for photos in tqdm(self._get_updated_list_of_files(os.listdir(self.ingestion_config.local_data_file_train+"/Normal"))):
                if get_size(Path(self.ingestion_config.local_data_file_train+f"/Normal/{photos}"))>0:
                    shutil.copy(self.ingestion_config.local_data_file_train+f"/Normal/{photos}",self.validation_config.validated_local_data_file_train+"/Normal")
                
            logger.info("Pneumonia train data send is going on..")
            for photos in tqdm(self._get_updated_list_of_files(os.listdir(self.ingestion_config.local_data_file_train+"/Viral Pneumonia"))):
                if get_size(Path(self.ingestion_config.local_data_file_train+f"/Viral Pneumonia/{photos}"))>0:
                    shutil.copy(self.ingestion_config.local_data_file_train+f"/Viral Pneumonia/{photos}",self.validation_config.validated_local_data_file_train+"/Viral Pneumonia")
            
            logger.info("Covid test data send is going on..")
            for photos in tqdm(self._get_updated_list_of_files(os.listdir(self.ingestion_config.local_data_file_test+"/Covid"))):
                if get_size(Path(self.ingestion_config.local_data_file_test+f"/Covid/{photos}"))>0:
                    shutil.copy(self.ingestion_config.local_data_file_test+f"/Covid/{photos}",self.validation_config.validated_local_data_file_test+"/Covid")
            
            logger.info("Normal test data send is going on..")
            for photos in tqdm(self._get_updated_list_of_files(os.listdir(self.ingestion_config.local_data_file_test+"/Normal"))):
                if get_size(Path(self.ingestion_config.local_data_file_test+f"/Normal/{photos}"))>0:
                    shutil.copy(self.ingestion_config.local_data_file_test+f"/Normal/{photos}",self.validation_config.validated_local_data_file_test+"/Normal")
                
            logger.info("Pneumonia test data send is going on..")
            for photos in tqdm(self._get_updated_list_of_files(os.listdir(self.ingestion_config.local_data_file_test+"/Viral Pneumonia"))):
                if get_size(Path(self.ingestion_config.local_data_file_test+f"/Viral Pneumonia/{photos}"))>0:
                    shutil.copy(self.ingestion_config.local_data_file_test+f"/Viral Pneumonia/{photos}",self.validation_config.validated_local_data_file_test+"/Viral Pneumonia")
            
        
        
                
                
                
        
        




















