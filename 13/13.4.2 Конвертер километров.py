# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах
# и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.

def convert_toMiles(km):
    return km * 0.6214


num = int(input())

print(convert_toMiles(num))