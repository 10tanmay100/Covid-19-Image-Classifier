from covid_classifier.components import PrepareBaseModel, prepare_base_model
from covid_classifier.components import DataValidation
from covid_classifier.entity import DataValidationConfig
from covid_classifier.entity import PrepareBaseModelConfig
from covid_classifier import logger
from covid_classifier.constants import *
from covid_classifier.utils import read_yaml
import os
from pathlib import Path
import glob
import shutil


class Test_prepare_base_model:
    data_validation_config=DataValidationConfig(
        root_dir="tests/data/Sample_validation/",
        validated_local_data_file="tests/data/Sample_validation/Covid19-dataset",
        validated_local_data_file_train="tests/data/Sample_validation/Covid19-dataset/train",
        validated_local_data_file_test="tests/data/Sample_validation/Covid19-dataset/test"
    )
    params_path=read_yaml(Path("E:/Ineuron/Project/Covid-19-Image-Classifier/params.yaml"))
    prepare_base_model=PrepareBaseModelConfig(
        root_dir="tests/data/Sample_base_model",
        base_model_path="tests/data/Sample_base_model/base_model.h5",
        updated_base_model_path="tests/data/Sample_base_model/updated_base_model.h5",
        params_image_size=params_path.IMAGE_SIZE,params_include_top=params_path.INCLUDE_TOP,params_weights=params_path.WEIGHTS,params_learning_rate=params_path.LEARNING_RATE,params_classes=params_path.CLASSES
    )
    def test_base_model(self):
        prepare_base=PrepareBaseModel(config=self.prepare_base_model,validation_path=self.data_validation_config)
        prepare_base.get_base_model()
        if os.path.exists(self.prepare_base_model.base_model_path):
            assert True
        else:
            assert False
    def test_updated_base_model(self):
        prepare_base=PrepareBaseModel(config=self.prepare_base_model,validation_path=self.data_validation_config)
        prepare_base.get_base_model()
        prepare_base.updated_base_model()
        if os.path.exists(self.prepare_base_model.updated_base_model_path):
            assert True
        else:
            assert False
