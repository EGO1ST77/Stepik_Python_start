import random
n = 100
a = [random.randint(-100, 100) for i in range(n)]

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(*a)
