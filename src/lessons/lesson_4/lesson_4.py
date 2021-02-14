# Команды для запуска из консоли:
# from lesson_4 import *
# docker_help()

from sys import argv

# workInHour, timeCost, bonus = argv

def docker_help():
  result = "Запускались все тестовые функции по порядку."



  print("Задача 4.7:")
  print(lesson_4_7())

  return result


def lesson_4_1():
    # Перенес в отдельный скрипт с номером 1, так же и для задания с 2мя скриптами
    print("Результат вычисления по исходной формуле: ", str(workInHour * timeCost + bonus))


def lesson_4_2():
    list_In = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    list_Out = [el for el in list_In if list_In[list_In.index(el)-1] < el and list_In.index(el) > 0]
    print(list_Out)


def lesson_4_3():
    listX = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
    print("Задача 4.3: ", str(listX))


def lesson_4_4():

    listX = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    map = {}

    def helper(arg):
        if(arg in map):
            return None
        else:
            map[arg] = arg
            return True

    listOut = [i for i in listX if helper(i) is True]

    return "Список без повторяющихся значений: " + str(listOut)


def lesson_4_5():
    result = 1

    def helper(arg):
        nonlocal result
        result = result * arg
        return arg

    def helper2(arg, arg2):
        return arg * arg2

    listX = [helper(i) for i in range(100, 1000) if i % 2 == 0]

    result = 0

    from functools import reduce
    result = reduce(helper2, listX)

    return "Задача 4.5: результат умножения: " + str(result)


def lesson_4_7():

    a = 10

    def fact(arg):
        for i in arg:
            n = 1
            factorial = 1
            # print("Вычисление нового факториала для числа: ", i)
            while n < i + 1:
                # print("f: ", factorial, ", n: ", n, ", f * n: ", factorial*n)
                factorial = factorial * n
                n += 1
            yield factorial

    args = range(1, a)
    print(args)
    factGenerator = fact(args)
    counter = 1
    for i in factGenerator:
        print("Факториал числа ", counter, ", равен: ", i, )
        counter += 1

    return 0

