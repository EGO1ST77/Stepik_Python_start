'''
На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nn, а затем n строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.
'''

n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for j in a:
    if j not in b:
        b.append(j)
print(b)


