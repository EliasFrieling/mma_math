'''
Created on Dec 28, 2018

@author: Elias
'''
import unittest
import sys
import fight_directory
from io import StringIO

class Test(unittest.TestCase):

    def test01(self):
        myDict = {'Randy Coture' : [['Pedro Rizzo', ['win', 'win']], ['Josh Barnett', ['loss']], ['sample', ['win']]]}
        myBool = fight_directory.is_rematch('Randy Coture', 'Josh Barnett', myDict)
        self.assertEqual(myBool, True)
    def test02(self):
        myDict = {'Randy Coture' : [['Pedro Rizzo', ['win', 'win']], ['Josh Barnett', ['loss']], ['sample', ['win']]]}
        myBool = fight_directory.is_rematch('Randy Coture', 'Pedro Rizzo', myDict)
        self.assertEqual(myBool, True)

if __name__ == "__main__":
    unittest.main()
