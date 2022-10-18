from gc import callbacks
from matplotlib import test
from covid_classifier.components import PrepareCallback
from covid_classifier.components import Training
from covid_classifier.entity import ModelTrainerConfig,PrepareCallbacksConfig
from covid_classifier import logger
from covid_classifier.constants import *
from covid_classifier.utils import read_yaml
import os
from pathlib import Path
import glob

class Test_model_trainer:
    params=read_yaml(Path("E:/Ineuron/Project/Covid-19-Image-Classifier/params.yaml"))
    callbacks=PrepareCallbacksConfig(
        root_dir="tests/data/Sample_prepare_callbacks",
        tensorboard_root_log_dir="tests/data/Sample_prepare_callbacks/tensorboard_dir/",
        checkpoint_model_filepath="tests/data/Sample_prepare_callbacks/ckpt_dir/"
    )
    trainer=ModelTrainerConfig(
        root_dir="tests/data/Sample_training",
        trained_model_path="tests/data/Sample_training/model.h5",
        updated_base_model_path="tests/data/Sample_base_model/updated_base_model.h5",
        training_data="tests/data/Sample_data/covid19-image-dataset/Covid19-dataset/train/",
        testing_data="tests/data/Sample_data/covid19-image-dataset/Covid19-dataset/test/",
        params_epochs=params.EPOCHS,params_TRAINING_batch_size=params.TRAINING_BATCH_SIZE,
        params_TESTING_batch_size=params.TESTING_BATCH_SIZE,params_is_augmentation=True,params_image_size=params.IMAGE_SIZE,params_target_size=params.TARGET_SIZE
    )
    def test_training(self):
        base_callback=PrepareCallback(
            config=self.callbacks
        )
        model_trainer=Training(
            config=self.trainer
        )
        model_trainer.get_base_model()
        model_trainer.train_valid_generator()
        model_trainer.train(callbacks_list=base_callback.get_tb_ckpt_callbacks())
        if os.path.exists(self.trainer.trained_model_path):
            assert True
        else:
            assert False
        