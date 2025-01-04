import numpy as np
import random

def generate_random_matrix(size):
    return np.random.randint(0, 10, size=(size, size))

def input_matrix(size):
    matrix = []
    print(f"Введите элементы матрицы {size}x{size} через пробел:")
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            print(f"Ошибка: введите ровно {size} элементов.")
            return None
        matrix.append(row)
    return np.array(matrix)

def main():
    matrix1 = None
    matrix2 = None
    result = None

    while True:
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            size = int(input("Введите размер квадратных матриц: "))
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = input("Выберите способ ввода: ")

            if input_method == '1':
                matrix1 = input_matrix(size)
                matrix2 = input_matrix(size)
            elif input_method == '2':
                matrix1 = generate_random_matrix(size)
                matrix2 = generate_random_matrix(size)
            else:
                print("Неверный выбор.")
                continue

            if matrix1 is not None and matrix2 is not None:
                print("Матрица 1:")
                print(matrix1)
                print("Матрица 2:")
                print(matrix2)
                result = None  # Сброс результата

        elif choice == '2':
            if matrix1 is not None and matrix2 is not None:
                result = matrix1 + matrix2
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:")
                print("Сумма матриц:")
                print(result)
                print("Определитель результата:")
                print(np.linalg.det(result))
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            print("Завершение работы программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")

if __name__ == "__main__":
    pass  # Заглушка для основной функции
