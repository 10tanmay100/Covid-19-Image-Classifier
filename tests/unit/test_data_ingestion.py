from covid_classifier.components import DataIngestion
from covid_classifier.entity import DataIngestionConfig
from covid_classifier import logger
import pytest
import os
import glob

class Test_data_ingestion:
    data_ingestion_config=DataIngestionConfig(
        root_dir='tests/data/Sample_data/',
        source_URL='https://raw.githubusercontent.com/10tanmay100/data_for_target_Sales/main/test_sample_data.zip',
        local_data_file='tests/data/Sample_data/sample_data.zip',
        local_data_file_train='tests/data/Sample_data/train',
        local_data_file_test='tests/data/Sample_data/test'
    )
    def test_dwld(self):
        data_ingestion=DataIngestion(config=self.data_ingestion_config)
        data_ingestion.download_data()
        if (os.path.exists(self.data_ingestion_config.local_data_file)) and len((glob.glob(self.data_ingestion_config.local_data_file_train)))>0 and len((glob.glob(self.data_ingestion_config.local_data_file_test)))>0:
            assert True
        else:
            assert False