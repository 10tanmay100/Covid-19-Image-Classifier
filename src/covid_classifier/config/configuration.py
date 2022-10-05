from logging import root
from covid_classifier.constants import *
from covid_classifier.entity import *
from covid_classifier.utils import *
from covid_classifier import logger

class ConfigurationManager:
    def __init__(self,config_path=CONFIG_FILE_PATH,params_path=PARAMS_FILE_PATH):
        self.config_path = read_yaml(config_path)
        self.params_path= read_yaml(params_path)
        create_directories([self.config_path.artifacts_root])
        logger.info("artifact directory created!!")
    def get_data_ingestion_config(self):
        config=self.config_path.data_ingestion
        create_directories([config.root_dir])
        logger.info("{config.root_dir} directory created!!")
        data_ingestion_config= DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,local_data_file=config.local_data_file,local_data_file_train=config.local_data_file_train,local_data_file_test=config.local_data_file_test)
        
        return data_ingestion_config
    
    def get_data_validation_config(self):
        config=self.config_path.data_validation
        create_directories([config.root_dir])
        logger.info("{config.root_dir} directory created!!")
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,validated_local_data_file=config.validated_local_data_file,validated_local_data_file_train=config.validated_local_data_file_train,validated_local_data_file_test=config.validated_local_data_file_test
        )
        return data_validation_config
        


