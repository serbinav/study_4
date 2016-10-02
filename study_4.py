# -*- coding: utf-8 -*-

import sys
import configparser
import datetime
import random

"""
    Задание по 4 лекции в прикрепленном документе.

    Для организации работы с консолью могут помочь материалы:

    https://stackoverflow.com/questions/16179875/command-line-input-in-python
    https://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments
    https://docs.python.org/2/library/functions.html#raw_input
    https://docs.python.org/3.5/library/functions.html#input
"""

# константы для формирования файла

class Product(object): #Продукт 
    name = None #Наименование
    measure = None #единицы измерения (килограммы, штуки, литры) 
    articleNumber = None #артикул 

    def __init__(self,nameProd, measureProd = "кг", articleNumberProd = 1409161500):
        self.name = nameProd
        self.measure = measureProd
        self.articleNumber = articleNumberProd

    def __hash__(self):
        return hash((self.name, self.measure, self.articleNumber))

    def __eq__(self, other):
        return (self.name, self.measure, self.articleNumber) == (other.name, other.measure, other.articleNumber)

    def __ne__(self, other):
        #return not (self == other)
        if not (self.name == other.name):
            return True
        elif not (self.measure == other.measure):
            return True
        elif not (self.articleNumber  == other.articleNumber):
            return True
        return False



class Storage(object): #Склад продуктов 
    listAvailableProduct = None #список доступных продуктов и их количество 

    def __init__(self):
        self.listAvailableProduct = dict()

    def generateCode(self):
        newSausage = Product("колбаса")
        self.listAvailableProduct[newSausage] = 100
        newCheese = Product("сыр")
        self.listAvailableProduct[newCheese] = 100
        newTomato = Product("помидоры")
        self.listAvailableProduct[newTomato] = 100
        return 0  # good

    def readFile(self,fileName):
        conf = configparser.RawConfigParser()
        conf.read(fileName)
        if 'storage' in conf:
            for key in conf['storage']:
                newProduct = Product(key)
                self.listAvailableProduct[newProduct] = conf['storage'].get(key)
            return 0 #good

        return 1 #bad

    def reserveProduct(self, newRecipe):
        for prod in newRecipe.listProduct:
            minusNumberPrоduct = int(self.listAvailableProduct[prod]) - int(newRecipe.listProduct[prod])
            self.listAvailableProduct[prod] = minusNumberPrоduct
        return 0  # good

    def printProduct(self):
        for element in self.listAvailableProduct:
            print(element.name + " " + str(self.listAvailableProduct[element]))



class Recipe(object): #Рецепт 
    title = None #оригинальное название
    listProduct = None #список продуктов и необходимое количество продуктов для приготовления пиццы 

    def __init__(self):
        self.title = random.randint(1, sys.maxsize)
        self.listProduct = dict()

    def addProduct (self,nameProduct,numberProduct): #добавлять продукты, указывая их количество
        pass

    def checkStorage(self,newStorage):
        if len(self.listProduct) > 0:
            for prod in self.listProduct:
                if int(self.listProduct[prod]) > int(newStorage.listAvailableProduct[prod]):
                    return 2  # bad
        else:
            return 1  # bad
        return 0  # good

    def checkDublicateProduct(self,newProduct,numberPrоduct):
        numberPrоduct = int(numberPrоduct)
        if newProduct in self.listProduct.keys():
            summNumberPrоduct = int(self.listProduct[newProduct]) + numberPrоduct
            self.listProduct[newProduct] = summNumberPrоduct
        else:
            self.listProduct[newProduct] = numberPrоduct

    def printProduct(self):
        print("название рецепта " + str(self.title))
        for element in self.listProduct:
            print(element.name + " " + str(self.listProduct[element]))

    def printError(self):
        pass



class Task(object): #Заказ
    listRecipe = None #список рецептов заказанных пицц 
    fullName= None #фио заказчика 
    date = None #дата заказа
    number = None #номер заказа

    def __init__(self,fullName): #создать заказ
        self.fullName = fullName
        self.date = datetime.datetime.now()
        number = iter(i for i in range(1, sys.maxsize))
        self.number = next(number)
        self.listRecipe = []

    def cancel(self): #удалить (отменить) заказ
        pass
    def change(self): #изменить заказ
        pass
    def addRecipe(self): #сформировать рецепты пицц
        pass
    def seeTask(self): #просмотреть существующие заказы с детализацией рецептов
        pass

    def printRecipe(self):
        print("фио заказчика " + self.fullName)
        print("дата заказа " + str(self.date))
        print("номер заказа " + str(self.number))
        for element in self.listRecipe:
            element.printProduct()

    def checkRecipe(self,titleRecipe):
        for rec in self.listRecipe:
            if titleRecipe == str(rec.title):
                return rec # good
        return 1  # bad

    def deleteRecipe(self,Recipe,newStorage):
        for prod in Recipe.listProduct:
            returnNumberPrоduct = int(newStorage.listAvailableProduct[prod]) + int(Recipe.listProduct[prod])
            newStorage.listAvailableProduct[prod] = returnNumberPrоduct
            Recipe.listProduct[prod] = 0

    def deleteTask(self, newStorage):
        for rec in self.listRecipe:
            self.deleteRecipe(rec, newStorage)
