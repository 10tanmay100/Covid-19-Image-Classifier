from scratch import *
import unittest
class Test_Method(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,10),20)
        self.assertEqual(add(20,1),21)
    def test_sub(self):
        self.assertEqual(substract(10,10),0)
        self.assertEqual(substract(20,1),19)
    def test_div(self):
        self.assertEqual(division(10,10),1.0)
        self.assertRaises(ZeroDivisionError,division,2,0)
    
        
    
if __name__ == '__main__':
    unittest.main()
        
     
