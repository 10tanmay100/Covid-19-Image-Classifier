import os
from zipfile import ZipFile
from covid_classifier.config import configuration
from covid_classifier.entity import DataIngestionConfig
from covid_classifier.entity import DataValidationConfig
from covid_classifier.entity import PrepareCallbacksConfig
from covid_classifier.entity import PrepareBaseModelConfig
from covid_classifier.entity import ModelTrainerConfig
from covid_classifier import logger
from covid_classifier.utils import *
from covid_classifier.constants import *
from keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm
from pathlib import Path
import tensorflow as tf
import keras
import shutil
import requests


class Training:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
    def get_base_model(self):
        self.model=tf.keras.models.load_model(self.config.updated_base_model_path)
        logger.info("Model Loaded for training!!!")
    def train_valid_generator(self):
        datagenerator_kwargs=dict(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
        training_dataflow_kwargs=dict(batch_size=self.config.params_TRAINING_batch_size,target_size =(224,224),seed=10,class_mode="categorical")
        
        testing_dataflow_kwargs=dict(batch_size=self.config.params_TESTING_batch_size,target_size = (224,224),seed=10,class_mode="categorical")
        logger.info("Data generatora defined!!! train {training_dataflow_kwargs} and test {testing_dataflow_kwargs}")
        
        if self.config.params_is_augmentation:
            train_datagen=ImageDataGenerator(**datagenerator_kwargs)
        else:
            train_datagen=ImageDataGenerator(rescale=1./255)
        test_datagen=ImageDataGenerator(rescale=1./255)
        
        
        self.train_generator=train_datagen.flow_from_directory(directory=self.config.training_data,**training_dataflow_kwargs)
        
        self.test_generator=test_datagen.flow_from_directory(directory=self.config.testing_data,**testing_dataflow_kwargs)
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    def train(self,callbacks_list:list):
        self.steps_per_epoch=self.train_generator.samples//self.train_generator.batch_size
        self.validation_steps=self.test_generator.samples//self.test_generator.batch_size
        
        self.model.fit(
            self.train_generator,steps_per_epoch=self.steps_per_epoch,epochs=self.config.params_epochs,validation_data=self.test_generator,validation_steps=self.validation_steps,callbacks=callbacks_list
        )
        logger.info("Model trained!!!")
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
        logger.info("Model Saved!!!")
    def evaluate(self):
        model=tf.keras.models.load_model(self.config.trained_model_path)
        self.score=model.evaluate(self.test_generator)
        with open("artifacts/model_training/score.txt", "w") as f:
            f.write(str({"loss":self.score[0],"accuracy":self.score[1]}))
        
      
      
    

            
        
    
    
    



