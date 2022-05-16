# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных
# по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
#
# Примечание 1. Списки list1 и list2 могут иметь разную длину.
#
# Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎

# объявление функции
def merge(list1, list2):
    list1.extend(list2)
    a = len(list1)
    for i in range(a-1):
        for j in range(i+1, a):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]

    return list1
# считываем данные
numbers1 = [int(c) for c in input('Первый список : ').split()]
numbers2 = [int(c) for c in input('Второй список : ').split()]

# вызываем функцию
print(merge(numbers1, numbers2))