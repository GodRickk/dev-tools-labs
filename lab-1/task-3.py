import numpy as np
import matplotlib.pyplot as plt
import cmath as m

# при х = -а будет достигаться минимум функции так как это парабола с ветвями вверх
def f_min(a):
    x = -a
    return x

def g_min(a, b):
    #обычная парабола
    if (b < 0):
        x = f_min(a)
        return x
    # все что ниже оси Ох отображается симмитрично неё
    # минимумы в точках пересечения графика с осями координат
    else:
        x_1 = (-(2 * a) + ((4 * b)**0.5)) / 2
        x_2 = (-(2 * a) - ((4 * b)**0.5)) / 2
        res = []
        res.append(x_1)
        res.append(x_2)
        return res

def solve(a, b):
    res = list()
    res.append(f_min(a))
    res.append(g_min(a, b))
    return res


a = float(input())
b = float(input())

res = solve(a, b)
print (res[0], res[1])