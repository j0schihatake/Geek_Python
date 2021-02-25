# Команды для запуска из консоли:
# from lesson_6 import *
# docker_help()

def docker_help():
  result = "Запускались все тестовые функции по порядку."
  lesson_6_1()
  return result


# -----------------------------------------------------Урок 1

# Задача 1:
def lesson_6_1():

    class TrafficLight:

        __color = None

        def getSec(self):
            import time
            now = time.ctime(1483391847.433716)
            parsed = time.strptime(now)
            return int(parsed.tm_sec)

        def running(self):
            start = self.getSec()
            current = 0
            while(current - start > 12):
                current = self.getSec()
                print(surrent)
                if(bool(current == 7)):
                    self.color = "красный"
                    print(TrafficLight.__color)
                elif(bool(currnet == 9)):
                    self.color = "желтый"
                    print(TrafficLight.__color)
                elif(bool(current == 11)):
                    self.color = "зеленый"
                    print(TrafficLight.__color)

    test = TrafficLight()
    test.running()
    return None