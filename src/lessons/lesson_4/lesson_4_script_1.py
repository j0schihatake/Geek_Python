from sys import argv

name, workInHour, timeCost, bonus = argv

def lesson_4_1():
    result = int(workInHour) * int(timeCost) + int(bonus)
    print("Результат вычисления по исходной формуле: ", result)

lesson_4_1()
