def add(x,y):
    return x + y

def multiply(x,y):
    return x * y


def division(x,y):
    if y==0:
        raise ZeroDivisionError
    else:
        return x / y

def substract(x,y):
    return x - y



class Employee:
    @classmethod
    def name(Employee):
        return "ok"
    raise_amt=1.54
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property
    def email(self):
        return f"{self.first} {self.last} mailed"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raises(self):
        self.pay=int(self.pay*self.raise_amt)

e=Employee("T","a",12)
print(Employee.name())
from pathlib import Path 
from box import ConfigBox
from covid_classifier.utils import *
print(isinstance(load_json(Path("tests/data/test1.json")),ConfigBox))

