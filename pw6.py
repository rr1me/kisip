def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

def find_max():
    num = int(input())
    if num == 0:
        return num
    next_max = find_max()
    return num if num > next_max else next_max

print("\n" + "=" * 20 + " БЛОК А " + "=" * 20)
print("Задача: Вычислить сумму цифр числа (4)")
print("Введите натуральное число:", end=" ")
number = int(input())
result_a = sum_digits(number)
print(f"Сумма цифр числа {number}: {result_a}")

print("\n" + "=" * 20 + " БЛОК Б " + "=" * 20)
print("Задача: Найти максимум в последовательности (1)")
print("Вводите числа по одному (завершите ввод нулём):")
result_b = find_max()
print(f"Наибольшее значение в последовательности: {result_b}")