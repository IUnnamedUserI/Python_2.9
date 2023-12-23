#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def accerman(m, n):
    """
    Функция принимает значения n и m, нужные для
    рассчёта значения функции Аккермана с помощью
    рекурсивных вызовов данного метода

    ПРЕДУПРЕЖДЕНИЕ: вводить значения больше 3 не рекомендуется
    """
    
    if m > 0 and n > 0:
        return accerman(m - 1, accerman(m, n - 1))
    elif m > 0 and n == 0:
        return accerman(m - 1, 1)
    elif m == 0:
        return n + 1

if __name__ == "__main__":
    n = input("Введите целочисленное число n: ")
    m = input("Введите целочисленное число m: ")
    result = 0
    if (n.isdigit() and m.isdigit()):
        n = int(n)
        m = int(m)
        result = accerman(m, n)
        print(f"Для n = {n} и m = {m} "
              f"значение функции Аккермана = {result}")
    else:
        print("Ошибка: одно из значений не является"
              "целочисленным и/или положительным числом")
        