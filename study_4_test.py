# -*- coding: utf-8 -*-
import unittest, study_4

"""
    Задание по 4 лекции в прикрепленном документе.

    Для организации работы с консолью могут помочь материалы:

    https://stackoverflow.com/questions/16179875/command-line-input-in-python
    https://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments
    https://docs.python.org/2/library/functions.html#raw_input
    https://docs.python.org/3.5/library/functions.html#input
"""

class Test(unittest.TestCase):

    def testDeleteDuplicate(self):
        #pass
        newStorage = study_4.Storage()
        newStorage.generateCode()

        newTask = study_4.Task()
        newTask.create()
        newTask.addRecipe()

        #self.assertEqual(study_4.MyParsingClass.deleteDuplicate(self,test),{1,2,3,4,5,6,7,8,10,9})

# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()

# ----------------------------------------------------------------------------------------------------
