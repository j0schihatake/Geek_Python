# Команды для запуска из консоли:
# from lesson_1 import *
# docker_help()

def docker_help():
  result = "docker_help: тестовые функции по порядку"
  print(lesson_1_1())
  return result

# ----------------------------------------------Урок 1

# Первая задача
def lesson_1_1():
  a = input("Введите значениепеременной a: ")
  b = input("Введите значениепеременной b: ")
  n = int(input("Введите значение числа n: "))
  c = '{0}{1}{2}{3}{4}{5}'.format("Вы ввели следующие значения: a = ", a, ", b = ", b, ", ну и наконец число n = ", n)
  return c

def lesson_1_2():
  return 0



# print('HelloWorld')


