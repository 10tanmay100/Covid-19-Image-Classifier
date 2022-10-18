
from covid_classifier.components import DataIngestion, data_ingestion
from covid_classifier.components import DataValidation
from covid_classifier.entity import DataIngestionConfig
from covid_classifier.entity import DataValidationConfig
from covid_classifier import logger
import pytest
import os
from pathlib import Path
import glob
import shutil


class Test_data_validation:
    data_validation_config=DataValidationConfig(
        root_dir="tests/data/Sample_validation/",
        validated_local_data_file="tests/data/Sample_validation/Covid19-dataset",
        validated_local_data_file_train="tests/data/Sample_validation/Covid19-dataset/train",
        validated_local_data_file_test="tests/data/Sample_validation/Covid19-dataset/test"
    ) 
    data_ingestion_config=DataIngestionConfig(
        root_dir='tests/data/Sample_data/',
        source_URL='https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset',
        local_data_file='tests/data/Sample_data/',
        local_data_file_train='tests/data/Sample_data/covid19-image-dataset/Covid19-dataset/train',
        local_data_file_test='tests/data/Sample_data/covid19-image-dataset/Covid19-dataset/test'
    )

    def test_check_data_gathering(self):
        os_check=[]
        data_ingestion=DataIngestion(config=self.data_ingestion_config)
        shutil.rmtree(Path("tests/data/Sample_data/covid19-image-dataset/Covid19-dataset/train/Normal/"))
        data_validation=DataValidation(ingestion_config=self.data_ingestion_config,validation_config=self.data_validation_config)
        os_check.append(data_validation.check_data_gathering())
        shutil.rmtree(Path("tests/data/Sample_data/covid19-image-dataset/"))
        data_ingestion.download_data()
        data_validation=DataValidation(ingestion_config=self.data_ingestion_config,validation_config=self.data_validation_config)
        os_check.append(data_validation.check_data_gathering())
        if (os_check[0]==False) and (os_check[1]==True):
            assert True
        else:
            assert False
    def test_dump_clean_data(self):
        data_validation=DataValidation(ingestion_config=self.data_ingestion_config,validation_config=self.data_validation_config)
        data_validation.check_data_gathering()
        data_validation.dump_clean_data()
        if (os.path.exists("tests/data/Sample_validation/Covid19-dataset/train")) and (os.path.exists("tests/data/Sample_validation/Covid19-dataset/test")):
            assert True
        else:
            assert False

