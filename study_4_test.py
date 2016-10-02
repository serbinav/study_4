# -*- coding: utf-8 -*-
import unittest
import study_4

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

    def testProduct(self):
        # pass
        p1 = study_4.Product('name1')
        p2 = study_4.Product('name2')
        p12 = study_4.Product('name1')
        assert p1 != p2
        assert p2 != p12
        assert p1 == p12
        assert hash(p1) == hash(p12)
        assert hash(p1) != hash(p2)
        assert hash(p2) != hash(p12)
        d = {p1: 10, p2: 5}
        d[p12] += 5
        d[p2] -= 5
        print(d)

# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()

# ----------------------------------------------------------------------------------------------------



