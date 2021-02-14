from lesson_4_script_3 import testCycle
from itertools import count
from sys import argv

name, inCount = argv

def getCount():
    next = range(int(inCount), 30)
    a = testCycle(next)
    print("Результат работы 2х скриптов: " + str(a))
    return 0

getCount()

