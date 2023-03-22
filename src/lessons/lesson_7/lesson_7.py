
def docker_help():
  result = "docker_help: тестовые функции по порядку"
  lesson_1()
  return result

def lesson_1():
    class Matrix:

        def __init__(self, params):
            self.param = params
            print(f"Создан новый обьект и в него передана матрица: {self.param}")

        def __str__(self):
            print(f"В данный обьект передали следующую матрицу: {self.param}")

        def __add__(self, other):
            for a in self.param:
                for b in self.param[a]:



    # Пример:
    param = [[1, 2, 3], [4, 5, 6]]
    m_1 = Matrix(param)

def lesson_2():

