'''
Created on Jul 25, 2014

@author: John
'''
import unittest
from gitTest import *


class Test(unittest.TestCase):


    def testName(self):
        self.assertEqual(get_Django_version(), "1.6.5")
        
    def testName2(self):
        self.assertEqual(get_Django_version(), "1.6.5")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()