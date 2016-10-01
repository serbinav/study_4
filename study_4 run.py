# -*- coding: utf-8 -*-

import sys
import copy
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

    if len(sys.argv) == 1:
        print("ошибка: не заданы входные параметры")
        sys.exit(1)

    newStorage = study_4.Storage()

    if int(sys.argv[1]) == 1:
        print("берем из кода")
        newStorage.generateCode()

    else:
        print("читаем из файла")
        newStorage.readFile("config.ini")

    #print(newStorage.listAvailableProduct.items())

    newTask = study_4.Task(input("введите ФИО: "))
    while True:
        yesNo = input("создать новый рецепт к заказу? (д/н) ")
        if yesNo == 'д':
            newRecipe = study_4.Recipe()
            print(newRecipe)

            noYes = 'д'
            while noYes != 'н':
                newStorage.printProduct()

                newProduct = study_4.Product(input("выбирает продукт из списка "))
                #print(newProduct.name)

                if newProduct in newStorage.listAvailableProduct.keys():
                    while True:
                        numberPrоduct = 0
                        numberPrоduct = input("введите количество ")

                        #print(numberPrоduct)
                        if numberPrоduct.isdigit():
                            # есть проблема когда один  продукт но 2 разных рецепта
                            newRecipe.checkDublicateProduct(newProduct,numberPrоduct)
                            print(newRecipe.listProduct.items())

                            break
                        else:
                            print("не числовой параметр введите заново")
                else:
                    print("неизвестный продукт")

                while True:
                    noYes = input("продолжаем ввод, добавляем еще продукты? (д/н) ")
                    if noYes == 'н':
                        yesNo = 'н'
                        # *********************
                        check = newRecipe.checkStorage(newStorage)
                        if check == 1:
                            print("в рецепт не добавлен продукт.")
                            break
                        elif check == 2:
                            print("нехватка продукта для приготовления рецепта.")
                            break

                        newTask.listRecipe.append(copy.copy(newRecipe))
                        newStorage.reserveProduct(newRecipe)

                        print(newStorage.listAvailableProduct.items())
                        # *********************
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
                    newTask.deleteRecipe(titleRecipe, newStorage)
                    print(newStorage.listAvailableProduct.items())
                    break
                elif delFin == 'з':
                    break
                else:
                    print("неизвестный аргумент")
            break
        else:
            print("неизвестный аргумент")

    # удалить заказа
    newTask.deleteTask(newStorage)

    print("смотрим склад")
    print(newStorage.listAvailableProduct.items())

    # print( newTask.fullName +" "+ str(newTask.date) +" "+ str(newTask.number))

    sys.exit(0)

# ----------------------------------------------------------------------------------------------------
