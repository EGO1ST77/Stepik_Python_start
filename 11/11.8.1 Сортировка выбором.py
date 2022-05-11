'''
Отсортируйте список по возрастанию, реализовав алгоритм сортировки выбором.
'''
import random
n = 100
a = [random.randint(-100, 100) for i in range(n)]

# через FOR
for i in range(n-1):
    m = i
    for j in range(i+1, n):
        if a[m] > a[j]:
            m = j
    a[i], a[m] = a[m], a[i]
print(*a)


