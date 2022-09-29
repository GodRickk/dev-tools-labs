import numpy as np

def linan(equ_1, equ_2):
  k_1 = equ_1.split()
  k_2 = equ_2.split()
  k_1 = [float(i) for i in k_1]
  k_2 =[float(i) for i in k_2]
  a = np.array([[k_1[0], k_1[1]], [k_2[0], k_2[1]]])
  b = np.array([k_1[2], k_2[2]])

  res = np.linalg.solve(a, b)
  return res
  pass

equ_1 = input()
equ_2 = input()
print(linan(equ_1, equ_2))