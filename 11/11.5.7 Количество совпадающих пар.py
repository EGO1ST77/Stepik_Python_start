'''
На вход программе подается строка текста, содержащая натуральные числа.
Из данной строки формируется список чисел. Напишите программу, которая подсчитывает,
сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести одно число – количество пар элементов, равных друг другу.
'''

s = input()
a = s.split()
for i in range(len(a)):
    count = 0
    count = a.count(a[i])
print(count)