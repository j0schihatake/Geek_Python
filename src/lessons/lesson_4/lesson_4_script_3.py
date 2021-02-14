from itertools import cycle

def testCycle(arg):
    print("testCycle() отработал.")
    listX = []
    count = 0
    iter = cycle(arg)

    while True:
        if count > 90:
            break
        listX.append(next(iter))
        count += 1

    # print(str(listX))
    return listX
