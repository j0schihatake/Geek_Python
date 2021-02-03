# Команды для запуска из консоли:
# from lesson_2 import *
# docker_help()

def docker_help():
  result = "docker_help: тестовые функции по порядку"
  print(lesson_2_2())
  return result

# ---------------------------------------------Урок 2:

# Задание 1
def lesson_2_1():
    result = "Типы в списке по порядку:"
    list = ["string", 3, True]
    for el in list:
        result += type(el)
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
    return result

