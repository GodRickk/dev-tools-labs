import numpy as np
def decorate_matrix(n):
    m = np.ones((n, n))
    m[1:n-1, 1:n-1] = 0
    return m


n = int(input())
print(decorate_matrix(n))