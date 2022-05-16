# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число
# и возвращающую количество делителей данного числа.
#
# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

def get_factors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

n = int(input())

print(get_factors(n))