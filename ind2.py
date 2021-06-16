#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    a = list(map(float, input("Введите список:").split()))
    c = float(input('Введите c: '))
    k = 0
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    s = 0
    for i in a:
        if i < c:
            s += 1
    n_0 = len(a)
    for i, item in reversed(list(enumerate(a))):
        if item < 0:
            n_0 = i
            break
    for z in a:
        k = sum(a[n_0 + 1:])
    f = str(sorted(a, key=lambda x: abs(x - max(a))))
    print(f"Количество элементов списка, меньших с --> {s}\nСумма после отрицательных элементов -- > {k}\n"
          f"Упорядоченный список: {f}")