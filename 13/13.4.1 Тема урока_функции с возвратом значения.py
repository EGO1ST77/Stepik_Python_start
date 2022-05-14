# Перевод градусов по Форенгейту в Цельсии
def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32)


# основная программа
temp = float(input("Введите градусы по Форенгейту : "))
celsius = convert_to_celsius(temp)
print(f'{temp} градусов по Форенгейту равны {celsius} по Цельсию')


# Функция с return - подсчет 100 бальной системы
def convret_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1


grade = int(input("Введите баш бал по 100-бальной системе : "))
print(f' Ваш бал = {convret_grade(grade)}')


# Длина гипотенузы прямоугольного треугольника

def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def get_distance(x1, y1, x2, y2):
    return compute_hypotenuse(x1 - x2, y1 - y2)


print(f'Длина гипотенузы сторон A и B = {compute_hypotenuse(5, 7)}')
print(f'Расстояние гипотинузы по точкам Х1, Х2, Y1, Y2 = {get_distance(1, 2, 3, 4)}')


# Функция, которая возвращает назад сумму цифр числа

def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result


n = int(input('Введи число : '))
print(f'Сумма чисел числа {n} равна {sum_digits(n)}')


# функция возвращает среднее значение элементов списка

def compute_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(compute_average(numbers))