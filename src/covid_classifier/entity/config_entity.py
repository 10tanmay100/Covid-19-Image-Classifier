from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    local_data_file_train:Path
    local_data_file_test:Path
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    validated_local_data_file:Path
    validated_local_data_file_train:Path
    validated_local_data_file_test:Path
