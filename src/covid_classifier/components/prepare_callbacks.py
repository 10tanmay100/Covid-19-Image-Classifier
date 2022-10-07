import time
import os
import urllib.request as request
from zipfile import ZipFile
from covid_classifier.entity import PrepareCallbacksConfig
import tensorflow as tf
from pathlib import Path



class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    @property
    def _create_earlystopping_callbacks(self):
        return tf.keras.callbacks.EarlyStopping(monitor='val_loss',
    min_delta=0,patience=5,verbose=0,mode='auto',baseline=None,restore_best_weights=False)

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks,
            self._create_earlystopping_callbacks
        ]