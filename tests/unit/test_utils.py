from covid_classifier.utils import *
import unittest
from pathlib import Path
from box import ConfigBox


first_yaml_path="tests/data/test1.yaml"
second_yaml_path="tests/data/test2.yaml"

class test_common_methods(unittest.TestCase):
    def test_read_yaml(self):
        self.assertEquals(read_yaml(Path(first_yaml_path)),ConfigBox({'data_ingestion': {'name': 'data_ingestion', 'date': '12/2/2022'}, 'data_validation': {'name': 'data_validation', 'date': '12/3/2022'}, 'model_training_': {'name': 'model_training_', 'date': '12/4/2022'}, 'model_evaluation': {'name': 'data_ingestion', 'date': '12/5/2022'}}))
        with self.assertRaises(ValueError):
            read_yaml(Path(second_yaml_path))
    
    def test_create_directories(self):
        if os.path.exists("tests/data/test_directories"):
            os.rmdir("tests/data/test_directories")
            os.makedirs("tests/data/test_directories",exist_ok=True)
            assert True
        else:
            os.makedirs("tests/data/test_directories",exist_ok=True)
            if os.path.exists("tests/data/test_directories"):
                assert True
            else:
                assert False
                
    def test_save_json(self):
        save_json(Path("tests/data/test2.json"),{"name":"Tanmay", "age":30, "project":"deep learning"})
        if os.path.exists("tests/data/test2.json"):
            assert True
        else:
            assert Exception("json is not available")
    
    def test_load_json(self):
        filedir,filename=os.path.split(Path("tests/data/test1.json"))
        if filename.split(".")[1]=="json":
            if isinstance(load_json(Path("tests/data/test1.json")),ConfigBox):
                assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()









