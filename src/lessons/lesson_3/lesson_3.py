# Команды для запуска из консоли:
# from lesson_3 import *
# docker_help()

# Запуск через докер:
# docker build -t hello-world .
# docker run -it --rm --name test_img hello-world

def docker_help():

   result = "Запускались все тестовые функции по порядку."

   print("Задача 1:")
   print(lesson_3_1())

   print("Задача 2:")
   print(lesson_3_2())

   print("Задача 3:")
   print(lesson_3_3())

   print("Задача 4:")
   print(lesson_3_4())

   print("Задача 5:")
   print(lesson_3_5())

   print("Задача 6:")
   print(lesson_3_6())

   return result

# -----------------------------------------------------Урок 3


def lesson_3_1():
    def test(arg1, arg2):
        try:
            result = arg1/arg2
            return result
        except Exception:
            return "Внимание при делении произошла ошибка."

    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))

    d = test(a, b)

    return "Задача 1: Результат деления: " + str(d)


def lesson_3_2():
    def userInfo(name, family, year, city, email):
        return "Информация о пользователе: name: " + str(name) + ", family: " + str(family) + ", year: " + year + ", city: " + city + ", email: " + email
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    year = input("Введите год: ")
    city = input("Введите город: ")
    email = input("Введие почту: ")

    return "Задача 2: " + str(userInfo(name, family, year, city, email))


def lesson_3_3():

    def my_func(*args):
        args = sorted(args)
        print(args)
        return args[2] + args[1]

    return "Задача 3: " + str(my_func(1, 7, 4))


def lesson_3_4():

    def my_func(x, y):
        i = 0
        while i < y:
            i = i + 1
            x = x + x*x
        return 1/x
    return "Задача 4, число в степени y = " + str(my_func(2.0, -1))

def lesson_3_5():

    work = True
    sum = 0

    while work == True:
        inp = input("Введите строку чисел разделенную пробелами")
        sp = inp.split()
        for el in sp:
            if el.isdigit():
                sum += int(el)
            else:
                try:
                    sum += float(el)
                except ValueError:
                    work = False
    return "Задача 5:" + str(sum)


def lesson_3_6():

    def int_func(arg):
        arg = arg.lower()
        a = arg[0]
        a = a.upper()
        arg = a + arg[1:]
        return arg

    return "Задача 6: " + str(int_func("ohohohi"))


