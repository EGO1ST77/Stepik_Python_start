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


