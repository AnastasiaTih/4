A = int(input('Введите размерность массива: '))
massiv_1 = []
for i in range(A):
     massiv_1.append(int(input('Введите число: ')))
     i += 1
print(massiv_1)
B = int(input('Введите размерность массива: '))
massiv_2 = []
for i in range(B):
     massiv_2.append(int(input('Введите число: ')))
     i += 1
print(massiv_2)
c = sorted(massiv_1 + massiv_2)
massiv_c = []
for i in range(len(c)):
     if c[i-1] == c[i]:
          massiv_c.append(c[i])
     i += 1
print(set(massiv_c))
