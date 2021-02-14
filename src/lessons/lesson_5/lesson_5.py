# Команды для запуска из консоли:
# from lesson_5 import *
# docker_help()

import json

def docker_help():
  result = "Запускались все тестовые функции по порядку."

  print("Задача 1:")
  print(lesson_5_1())

  return result

# -----------------------------------------------------Урок 5

def lesson_5_1():
    ins = 1
    helper = 0
    listIn = list()
    while ins == 1:
        a = str(input("Введите значение: "))
        if not a:
            print("Выполняем запись в файл:")
            file = open("file_1", "w")
            print(listIn)
            for el in listIn:
                file.write(str(el))
            file.close()
            ins = 0
        else:
            listIn.append(a + "\n")

        helper += 1
        if helper > 10:
            ins = 0
    return 0


def lesson_5_2():
    file = open("file_2", "r")
    work = True
    counter = 1                     # Счетчик числа строк
    listLine = list()
    while work:
        line = file.readline()
        if not line:
            work = False
        # разрезаем строку и считем слова:
        n = line.split(" ")
        print(line)
        listLine.append(len(n))
        counter += 1
    file.close()

    print("Число строк в файле: ", counter)
    iter = 1
    for el in listLine:
        print("В строке ", iter, " число слов равно: ", el)
        iter+=1
    return 0

def lesson_5_3():
    file = open("file_3", "r")
    low = {}

    counter = 0
    sum = 0

    work = True

    while work:
        counter += 1
        line = file.readline()
        if not line:
            work = False
        n = line.split(" ")
        print(n)
        name = n[0]
        print(name)
        if not name:
            print("Пустая строка")
        else:
            value = int(n[1])

        sum += value

        if value < 20:
            low[name] = value

    file.close()

    print("Фамилии сотрудников с окладом меньше 20: ")
    for elV, elK in low.items():
        print(elV, " имеет зп = ", elK)

    print("Среднее значение зарпалты сотрудников: ", sum/counter)

    return 0

def lesson_5_4():
    file = open("file_4", "r")
    mapper = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    all = {}
    work = True
    while work:
        line = file.readline()
        if not line:
            work = False
        line.replace("\n", "")
        n = line.rsplit(" ")
        name = n[0]
        if not name:
            print("Пустая строка")
        else:
            name = mapper[str(name)]
            all[name] = ""
            value = int(n[2])
            all[name] = value

    file.close()

    # Записываем в file_4_out:
    fileOut = open("file_4_out", "w")
    for elV, elK in all.items():
        fileOut.write(str(elK) + " " + str(elV))
    fileOut.close()
    print("all: ", all)
    return 0

def lesson_5_5():
    # запись:
    file = open("file_5", "w")
    line = ""
    for i in range(30):
        line = line + str(i) + " "
    file.write(line)
    file.close()

    # Считывание:
    readFile = open("file_5", "r")
    work = True
    summ = 0
    while work:
        line = readFile.readline()
        if not line:
            work = False
        line = line.split(" ")
        for i in line:
            if i:
                summ += int(i)
    readFile.close()
    print("Сумма чисел: ", summ)
    return 0

def lesson_5_6():
    result = {}
    file = open("file_6", "r", encoding='UTF8')
    work = True
    summ = 0
    while work:
        line = file.readline()
        if not line:
            work = False

        line = line.replace("(л)", "")
        line = line.replace("(пр)", "")
        line = line.replace("(лаб)", "")
        line = line.replace("-", "")
        line = line.replace("\n", "")
        line = line.split(" ")

        index = 0
        name = ""
        for i in line:
            if i:
                if index < 1:
                    name = line[0]
                else:
                    n = int(i) if i.isdigit() else float(i) if i.replace('.', '').isdigit() else i
                    summ += int(n)
                    result[name] = summ
                index += 1
    file.close()

    for iK, iV in result.items():
        print("По дисциплине: ", str(iK), " число занятий ", str(iV))
    return 0

def lesson_5_7():
    file = open("file_7", "r", encoding='UTF8')
    work = True

    firms = {}

    while work:
        line = file.readline()
        if not line:
            work = False

        line = line.replace(".", "")
        line = line.replace("\n", "")
        line = line.split(" ")

        index = 0
        name = ""
        type = ""
        apBonus = 0
        disapBonus = 0
        for i in line:
            if i:
                if index < 1:
                    name = str(line[0])
                elif index == 1:
                    type = str(line[index])
                elif index == 2:
                    apBonus = int(line[index])
                elif index == 3:
                    disapBonus = int(line[index])
            index+=1
        firms[name] = [type, apBonus, disapBonus]

        print("firms: ", firms)

        itog = {}
        # Рассчеты:
        for iK, iV in firms.items():
            print("iV: ", iV)
            a = iV[1]
            b = iV[2]
            print("a: ", a, ", b: ", b)
            prib = int(a) - int(b)
            print("prib = ",prib)
            itog[iK] = prib
            # непонятно как среднюю прибыль одной компании посчитать, не стал считать)
    file.close()

    with open("json_example.json", "w") as jsons:
        json.dump(itog, jsons)
    return 0

lesson_5_7()
