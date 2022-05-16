# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число
# и возвращающую список всех делителей данного числа.

def get_factors(num):
    d = []
    for i in range(1, num+1):
        if num % i == 0:
            d.append(i)
    return d

n = int(input())

print(get_factors(n))