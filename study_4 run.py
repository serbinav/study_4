# -*- coding: utf-8 -*-

import sys
import study_4

"""
    Задание по 4 лекции в прикрепленном документе.

    Для организации работы с консолью могут помочь материалы:

    https://stackoverflow.com/questions/16179875/command-line-input-in-python
    https://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments
    https://docs.python.org/2/library/functions.html#raw_input
    https://docs.python.org/3.5/library/functions.html#input
"""

# константы для формирования файла

# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    newStorage = study_4.Storage()

    codeHdd = None
    while codeHdd != 'к' or codeHdd != 'ф':
        codeHdd = input("загрузить продукты на склад из коде приложения или из файла на жестком диске? (к/ф) ")
        if codeHdd == 'к':
            print("берем из кода")
            newStorage.generateCode()
            break
        elif codeHdd == 'ф':
            print("читаем из файла")
            if newStorage.readFile("config.ini") == 0:
                break
            else:
                print("файл config.ini не найден")
                sys.exit(1)
        else:
            print("неизвестный аргумент")

    newStorage.printProduct()

    listTask = []
    flagTask = None
    while flagTask != 'н':
        flagTask = input("создать новый заказ? (д/н) или вывести на экран существующие заказы (п), "
                         "или удалить заказ (у) ")
        if flagTask == 'д':
            newTask = study_4.Task(input("введите ФИО: "))
            listTask.append(newTask)
            while True:
                yesNo = input("создать новый рецепт к заказу? (д/н) ")
                if yesNo == 'д':
                    newRecipe = study_4.Recipe()

                    noYes = 'д'
                    while noYes != 'н':
                        newStorage.printProduct()

                        newProduct = study_4.Product(input("выбирает продукт из списка "))

                        if newProduct in newStorage.listAvailableProduct.keys():
                            while True:
                                numberPrоduct = 0
                                numberPrоduct = input("введите количество ")
                                if numberPrоduct.isdigit():
                                    newRecipe.checkDublicateProduct(newProduct, numberPrоduct)
                                    break
                                else:
                                    print("не числовой параметр введите заново")
                        else:
                            print("неизвестный продукт")

                        while True:
                            noYes = input("продолжаем ввод, добавляем еще продукты? (д/н) ")
                            if noYes == 'н':
                                yesNo = 'н'
                                check = newRecipe.checkStorage(newStorage)
                                if check == 1:
                                    print("в рецепт не добавлен продукт.")
                                    break
                                elif check == 2:
                                    print("нехватка продукта для приготовления рецепта.")
                                    break

                                newTask.listRecipe.append(newRecipe)
                                newStorage.reserveProduct(newRecipe)
                                break
                            elif noYes == 'д':
                                break
                            else:
                                print("неизвестный аргумент")

                elif yesNo == 'н':
                    delFin = None
                    while delFin != 'з':
                        delFin = input("удалить рецепт из заказа или завершить работу с этим заказом? (у/з) ")
                        if delFin == 'у':
                            titleRecipe = newTask.printRecipe()
                            delRecipeFlag = None
                            while not delRecipeFlag:
                                titleRecipe = input("введите название рецепта ")
                                delRecipeFlag = newTask.checkRecipe(titleRecipe)
                                if delRecipeFlag == 1:
                                    print("неизвестное название")
                                    delRecipeFlag = False
                                else:
                                    newTask.deleteRecipe(delRecipeFlag, newStorage)
                                    delRecipeFlag = True
                                    break
                            break
                        elif delFin == 'з':
                            break
                        else:
                            print("неизвестный аргумент")
                    break
                else:
                    print("неизвестный аргумент")
        elif flagTask == 'п':
            for Task in listTask:
                Task.printRecipe()
        elif flagTask == 'у':
            delTask = None
            while not delTask:
                numberTask = input("введите номер заказа (для выхода напишите - в) ")
                if numberTask == 'в':
                    delTask = True
                for task in listTask:
                    if numberTask == str(task.number):
                        task.deleteTask(newStorage)
                        listTask.remove(task)
                        delTask = True
                        break
                if not delTask:
                    print("неизвестный номер заказа")
                    delTask = False
        elif flagTask == 'н':
            break
        else:
            print("неизвестный аргумент")

    sys.exit(0)

# ----------------------------------------------------------------------------------------------------
