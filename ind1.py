#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    A = list(map(int, input('Введите 10 элементов: ').split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = 0
    k = 0
    for i in A:
        if (i % 5) == 0:
            s += i
    print(f"Сумма элементов кратных 5 : {s}")
    for n in A:
        if (n % 5) == 0:
            k += 1
    print(f"Количество элементов кратных пяти : {k}")