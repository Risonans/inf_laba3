import numpy as np

# Функция сортировки пузырьком по возрастанию и убыванию
# Принимает mas, x
# Возвращает список из чисел
# Пример: [3, 2, 1, 7], 1 -> [1, 2, 3, 7]; [3, 2, 1, 7], 2 -> [7, 3, 2, 1]
# Классы эквивалентности: массивы, буквы, цифры, специальные символы
# Граничные значения по int
def bubble(mas, x):
    if mas == []: return 0
    if x == 1:
        for i in range(len(mas) - 1):
            for j in range(len(mas) - 1 - i):
                if mas[j] > mas[j + 1]:
                    mas[j], mas[j + 1] = mas[j + 1], mas[j]
        return mas
    if x == 2:
        for i in range(len(mas) - 1):
            for j in range(len(mas) - 1 - i):
                if mas[j] < mas[j + 1]:
                    mas[j], mas[j + 1] = mas[j + 1], mas[j]
        return mas

print("Введите массив и выберите как его отсортировать (1 - по возрастанию / 2 - по убыванию))")
a = input("Массив: ")
mas = a_string.split()
x = int(input("выбери как сортировать: "))