a = int(input('Введите размерность массива: '))
massiv = []
for i in range(a):
     massiv.append(float(int(input('Введите число: '))))
     i += 1
print(massiv)
b = massiv.index(max(massiv))
for i in range(b+1, a):
    massiv[i]=0
print(massiv)