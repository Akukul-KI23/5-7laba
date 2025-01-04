import numpy as np
import random

def generate_random_matrix(size):
    return np.random.randint(0, 10, size=(size, size))

def input_matrix(size):
    # Заглушка для ввода матрицы
    print(f"Заглушка: Ввод матрицы {size}x{size}")
    return generate_random_matrix(size)

def display_matrix(matrix, name):
    # Заглушка для отображения матрицы
    print(f"Заглушка: Отображение матрицы {name}")
    pass

def sum_matrices(matrix1, matrix2):
    # Заглушка для суммирования матриц
    print("Заглушка: Суммирование матриц")
    return matrix1 + matrix2

def calculate_determinant(matrix):
    # Заглушка для вычисления определителя матрицы
    print("Заглушка: Вычисление определителя матрицы")
    return np.linalg.det(matrix)

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

        # Заглушка для выбора пункта меню
        choice = '1'  # Заглушка: всегда выбираем пункт 1

        if choice == '1':
            size = 3  # Заглушка: размер матрицы 3x3
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = '2'  # Заглушка: всегда выбираем случайный ввод

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
                display_matrix(matrix1, "Матрица 1")
                display_matrix(matrix2, "Матрица 2")
                result = None  # Сброс результата

        elif choice == '2':
            if matrix1 is not None and matrix2 is not None:
                result = sum_matrices(matrix1, matrix2)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:")
                display_matrix(result, "Сумма матриц")
                determinant = calculate_determinant(result)
                print(f"Определитель результата: {determinant}")
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            print("Завершение работы программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")

        # Заглушка для завершения цикла после одного прохода
        break

if __name__ == "__main__":
    main()
