'''
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
s = input()
out = ''
for i in s.split():
    out += i[0]+'.'
print(out)

input = "Self contained underwater breathing apparatus"
output = ""
for i in input.upper().split():
    output += i[0]
print(output)