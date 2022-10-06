import os
from zipfile import ZipFile
from covid_classifier.config import configuration
from covid_classifier.entity import DataIngestionConfig
from covid_classifier.entity import DataValidationConfig
from covid_classifier.entity import PrepareBaseModelConfig
from covid_classifier import logger
from covid_classifier.utils import *
from covid_classifier.constants import *
from pathlib import Path
import requests
import tensorflow as tf
import keras
from keras.models import Model
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Activation, Dropout
from keras.layers import Dense
from keras.preprocessing import image
from keras.utils import load_img
from keras.utils import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from glob import glob





class PrepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config_file_path=read_yaml(CONFIG_FILE_PATH)
        self.params_file_path=read_yaml(PARAMS_FILE_PATH)
        self.validated_file_path=DataValidationConfig
        self.config=config
        
    def get_base_model(self):
        logger.info("Base model creaetion has been started!!!")
        self.base_model=VGG16(include_top=self.config.params_include_top,input_shape=self.config.params_image_size+[3],weights=self.config.params_weights)
        self.save_model(path=self.config.base_model_path,model=self.base_model)
        logger.info(f"Base mode saved in the location {self.config.base_model_path}")
    
    
    @staticmethod
    def _prepare_complete_model(model,classes:int,freeze_all:bool,freeze_till,learning_rate:float):
            if freeze_all==True:
                for layer in model.layers:
                    layer.trainable=False
            else:
                if (freeze_till is not None) and (freeze_till > 0):
                    for layer in model.layers[:-freeze_till]:
                        layer.trainable=False
            x=Flatten()(model.output)
            prediction=Dense(units=classes,activation="softmax")(x)
            full_model=Model(inputs=model.input,outputs=prediction)
            optimizer=tf.optimizers.Adam(learning_rate=learning_rate)
            full_model.compile(optimizer=optimizer,loss="categorical_crossentropy",metrics=["accuracy"])
            full_model.summary()
            return full_model
    def updated_base_model(self):
        logger.info("Base model updation has been started!!!")
        updated_model=self._prepare_complete_model(model=self.base_model,classes=self.config.params_classes,freeze_all=True,freeze_till=None,learning_rate=self.config.params_learning_rate)
        self.save_model(path=self.config.updated_base_model_path,model=updated_model)
        logger.info(f"Updated model saved at {self.config.updated_base_model_path}")
        return "Model Saved!!!!"                            
        
    
    @staticmethod
    def save_model(path:Path,model):
        model.save(path)
        
        
    












