from covid_classifier.components import PrepareBaseModel
from covid_classifier.config import ConfigurationManager
from covid_classifier import logger



def main():
    config=ConfigurationManager()
    prepare_base_model_config=config.get_prepare_base_model_config()
    preparebasemodel=PrepareBaseModel(config=prepare_base_model_config)
    preparebasemodel.get_base_model()
    print(preparebasemodel.updated_base_model())





STAGE_NAME="prepare_base_model"
if __name__=="__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} has started <<<<<<<")
        main()
        logger.info(f">>>>>>> {STAGE_NAME} has ended <<<<<<<")
    except Exception as e:
        raise e