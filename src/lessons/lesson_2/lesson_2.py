# Команды для запуска из консоли:
# from lesson_2 import *
# docker_help()

def docker_help():
  result = "docker_help: тестовые функции по порядку"
  print(lesson_2_1())
  print(lesson_2_2())
  print(lesson_2_3())
  print(lesson_2_4())
  print(lesson_2_5())
  print(lesson_2_6())
  return result

# ---------------------------------------------Урок 2:

# Задание 1
def lesson_2_1():
    result = "Типы в списке по порядку:"
    list = ["string", 3, True]
    for el in list:
        result += str(type(el))
    return result

# Задание 2
def lesson_2_2():
    list = ["элемент1", "элемент2", "элемент3", "элемент4", "элемент5"]
    count = len(list);
    i = 0
    while(i < count):
        n = i % 2
        if(n > 0):
            elFirst = list[i-1]
            elTwo = list[i]
            list[i-1] = elTwo
            list[i] = elFirst
        i = i + 1
    return list

# Задание 3
def lesson_2_3():
    month = int(input("Введите месяц"))
    if(month > 12 | month <= 0):
        print("Ошибка вы ввели неправильный месяц.")

    if(month > 11 & month < 3):
        type = 0
    elif(month > 2 & month < 6):
        type = 1
    elif (month > 5 & month < 9):
        type = 2
    elif(month > 8 & month < 12):
        type = 3

    fromList = ["зима", "весна", "лето", "осень"]
    fromDict = {0:"зима", 1:"весна", 2:"лето", 3:"осень"}

    print("Решение через list: искомый месяц пренадлежит следующему времени года: " + fromList[type])
    print("Решение через dict: искомый месяц пренадлежит следующему времени года: " + fromDict[type])

    return "Врямя года: list - " + fromList[type] + ", dict = " + fromDict[type]

# Задание 4
def lesson_2_4():
    inp = input("Введите строку со словами,разделитель пробел")
    list = inp.split()

    for el in list:
        print("Под номером - " + str(list.index(el)) + ":" + el[0:10])
    return 0

# Задание 5
def lesson_2_5():
    my_list = [7, 5, 3, 3, 2]
    inp = int(input("Введите новый элементрейтинга"))
    my_list.append(inp)
    my_list.sort(reverse=True)
    return my_list

# Задание 6
def lesson_2_6():

    store = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
            (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
            (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]

    valueFromKeyMap = {}

    for el in store:
        print(type(el))
        if isinstance(el, tuple):
            valueDict = el[1]
            print(type(valueDict))
            if isinstance(valueDict, dict):
                for key, value in valueDict.items():
                    print(key in valueFromKeyMap)
                    if(key in valueFromKeyMap):
                        valueList = valueFromKeyMap[key]
                        valueList.append(value)
                    else:
                        valueList = [value]
                    valueFromKeyMap[key] = list(set(valueList))
            else:
                print("Ошибка. Не верен ожидаемый тип содержимого. Ожидаем dict.")
        else:
            print("Ошибка. Не верен ожидаемый тип содержимого. Ожидаем tuple.")
    return "Результат задачи по сбору статистики о предметах во вложенных структурах: " + str(valueFromKeyMap)