"""
Дано натуральное число N. Выведите все его цифры по одной, в обратном
порядке, разделяя их пробелами или новыми строками. При решении этой
задачи нельзя использовать строки, списки, массивы. Разрешена только
рекурсия и целочисленная арифметика.
"""


def print_digits(n):
    if n > 0:
        last_digit = n % 10
        print(last_digit, end=" ") # 

        print_digits(n // 10) #



N = int(input("Введите N: "))
print("Цифры числа", N, "в обратном порядке: ", end="")
print_digits(N)
