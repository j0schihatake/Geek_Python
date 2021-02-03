from datetime import datetime

# Команды для запуска из консоли:
# from lesson_1 import *
# docker_help()

def docker_help():
  result = "Запускались все тестовые функции по порядку."

  print("Задача 1:")
  print(lesson_1_1())

  print("Задача 2:")
  print(lesson_1_2())

  print("Задача 3:")
  print(lesson_1_3())

  print("Задача 4:")
  print("Максимальная из введенных цифр: ", lesson_1_4())

  print("Задача 5:")
  print("Прибыль фирмы на одного сотрудника: ", lesson_1_5())

  print("Задача 6:")
  print("Искомый результат будет достигнут при продолжении тренеровок через ", lesson_1_6())

  return result

# -----------------------------------------------------Урок 1

# Задача 1:
def lesson_1_1():
  a = input("Введите значениепеременной a: ")
  b = input("Введите значениепеременной b: ")
  n = int(input("Введите значение числа n: "))
  c = '{0}{1}{2}{3}{4}{5}'.format("Вы ввели следующие значения: a = ", a, ", b = ", b, ", ну и наконец число n = ", n)
  return c

# Задача 2:
def lesson_1_2():
  inp = int(input("Введите дату в секундах: "))
  time = datetime.fromtimestamp(inp).strftime("%I:%M:%S")
  return time

# Задача 3:
def lesson_1_3():
  inp = int(input("Введите которое требуется рассчитать по формуле n + nn + nnn:"))
  result = inp + inp*inp + inp*inp*inp
  return result

# Задача 4:
def lesson_1_4():
  find = True
  inp = input("Введите число в котором необходимо найти самую большую цифру:")
  inpList = list(inp)
  max = 0
  i = 0
  while find:
    next = inpList[i]
    if int(next) > max:
      max = int(next)
    i += 1
    if len(inpList) == i:
      find = False
  return max

# Задание 5:
def lesson_1_5():
  oneHumanBuf = 0

  # значения выручки и издержек фирмы
  buf = int(input("Введите значение выручки фирмы:"))
  debuf = int(input("Введите значение издержек фирмы:"))

  # прибыль — выручка больше издержек, или убыток — издержки больше выручки
  if buf > debuf:
    print("Фирма является прибыльным предприятием.")
    ren = buf/debuf
    humanCount = int(input("Введите численность сотрудников фирмы:"))
    oneHumanBuf = buf/humanCount
  else:
    print("Фирма является убыточным предприятием.")
  return oneHumanBuf

# Задание 6:
def lesson_1_6():
  nextResult = int(input("Введите успешность результатов тренеровок первого дня: "))
  b = int(input("Введите желаемый результат тренеровок: "))
  buf = 0.1
  foundDay = 1
  while(nextResult < b):
    nextResult = nextResult + nextResult * buf
    foundDay = foundDay + 1
  return foundDay
