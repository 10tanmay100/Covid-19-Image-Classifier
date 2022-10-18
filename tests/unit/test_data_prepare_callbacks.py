# from covid_classifier.components import PrepareBaseModel,PrepareCallback
# from covid_classifier.components import DataValidation
# from covid_classifier.entity import DataValidationConfig
# from covid_classifier.entity import PrepareBaseModelConfig
# from covid_classifier import logger
# from covid_classifier.constants import *
# from covid_classifier.entity.config_entity import PrepareCallbacksConfig
# from covid_classifier.utils import read_yaml
# import os
# from pathlib import Path
# import glob
# import shutil



# class Test_prepare_base_callback:
#     callbacks=PrepareCallbacksConfig(
#         root_dir="tests/data/Sample_prepare_callbacks",
#         tensorboard_root_log_dir="tests/data/Sample_prepare_callbacks/tensorboard_dir",
#         checkpoint_model_filepath="tests/data/Sample_prepare_callbacks/ckpt_dir"
#     )
#     def test_ckpt_model(self):
#         base_callback=PrepareCallback(
#             config=self.callbacks
#         )
#         base_callback.get_tb_ckpt_callbacks()
#         if len(os.listdir(self.callbacks.tensorboard_root_log_dir))>0 and len(os.listdir(self.callbacks.checkpoint_model_filepath))>0:
#             assert True
#         else:
#             assert False
