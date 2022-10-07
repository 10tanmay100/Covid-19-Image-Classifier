from logging import root
from venv import create
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
    def get_prepare_base_model_config(self):
        config=self.config_path.prepare_base_model
        create_directories([config.root_dir])
        logger.info(f"{config.root_dir} directory created")
        prepare_base_model_config=PrepareBaseModelConfig(
            root_dir=config.root_dir,base_model_path=config.base_model_path,updated_base_model_path=config.updated_base_model_path,params_image_size=self.params_path.IMAGE_SIZE,params_include_top=self.params_path.INCLUDE_TOP,params_weights=self.params_path.WEIGHTS,params_learning_rate=self.params_path.LEARNING_RATE,params_classes=self.params_path.CLASSES
        )
        return prepare_base_model_config
        
    def get_prepare_callbacks_config(self):
        config=self.config_path.prepare_callbacks
        create_directories([config.root_dir])
        logger.info(f"Prepare callbacks directory created")
        prepare_callbacks_config=PrepareCallbacksConfig(
            root_dir=config.root_dir,tensorboard_root_log_dir=
            config.tensorboard_root_log_dir,checkpoint_model_filepath=config.checkpoint_model_file_path
        )
        return prepare_callbacks_config
    def get_training_config(self,data_validation_config) -> ModelTrainerConfig:
        training = self.config_path.model_training
        prepare_base_model = self.config_path.prepare_base_model
        params = self.params_path
        training_data = data_validation_config.validated_local_data_file_train
        testing_data=data_validation_config.validated_local_data_file_test
        create_directories([
            Path(training.root_dir)
        ])

        training_config = ModelTrainerConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            testing_data=Path(testing_data),
            params_epochs=params.EPOCHS,
            params_TRAINING_batch_size=params.TRAINING_BATCH_SIZE,
            params_TESTING_batch_size=params.TESTING_BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_target_size=params.TARGET_SIZE
        )

        return training_config
        


