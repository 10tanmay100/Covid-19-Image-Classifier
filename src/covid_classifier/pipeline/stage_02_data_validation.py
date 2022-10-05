from covid_classifier.components import DataValidation
from covid_classifier.config import ConfigurationManager
from covid_classifier import logger



def main():
    config=ConfigurationManager()
    data_ingestion_config=config.get_data_ingestion_config()
    data_validation_config=config.get_data_validation_config()
    data_validation=DataValidation(ingestion_config=data_ingestion_config,validation_config=data_validation_config)
    data_validation.check_data_gathering()
    data_validation.dump_clean_data()





STAGE_NAME="data_validation"
if __name__=="__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} has started <<<<<<<")
        main()
        logger.info(f">>>>>>> {STAGE_NAME} has ended <<<<<<<")
    except Exception as e:
        raise e