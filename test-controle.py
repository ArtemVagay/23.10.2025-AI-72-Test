# Вагайцев Артем Дмитриевич Сложный Уровень
# 1
# import math
# while True:
#     try:
#         matrix_size = int(input("Введите размер для треугольника используя нечетные числа (минимум 3): "))
#         if matrix_size > 2 and matrix_size % 2 != 0:
#             break
#         print("Попробуйте еще раз!")
#     except:
#         print("Попробуйте еще раз!")
# matrix = [[" " for i in range(matrix_size)] for j in range(matrix_size)]
# for x in range(matrix_size):
#     for y in range(matrix_size):
#         if (x == matrix_size or x == matrix_size - 1 or x == y or y == matrix_size - x - 1) and x > matrix_size // 2 - 1:
#             matrix[x - matrix_size // 2][y] = "*"
#     print()
#
# for row in matrix:
#     for element in row:
#         print(element, end=' ')
#     print()
#
# 2
# while True:
#     try:
#         a = int(input("Введите число: "))
#         b = int(input("Введите первое значение для промежутка: "))
#         c = int(input("Введите второе значение для промежутка: "))
#         break
#     except:
#         print("Попробуйте еще раз!")
#
# if a <= c or a >= b:
#     print(f'Число {a} принадлежит промежутку [{b}, {c}]')
