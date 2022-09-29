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

def f_x(x, a, b):
    return ((x + a)**2) - b

def g_x(x, a, b):
    return abs(f_x(x, a, b))

def solve(a, b):
    res = list()
    res.append(f_min(a))
    res.append(g_min(a, b))
    return res


a = float(input())
b = float(input())

res = solve(a, b)
print (res[0], res[1])
print("------------------------------")

m = np.arange(f_min(a) - 4, f_min(a) + 4.01, 0.01)

plt.plot(m, (((m + a)**2) - b))
plt.plot(m, abs((((m + a)**2) - b)), "r--")
plt.plot(f_min(a), f_x(f_min(a), a, b), "bo")
plt.plot(g_min(a, b)[0], g_x(g_min(a, b)[0], a, b), "ro")
plt.plot(g_min(a, b)[1], g_x(g_min(a, b)[1], a, b), "ro")
plt.show()