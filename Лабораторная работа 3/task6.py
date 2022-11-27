list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = 0
max_number = list_numbers[max_i]

for i, current_number in enumerate(list_numbers):  # переберем все индексы чисел до последнего
    if current_number >= max_number:  # если текущее число больше того, что встречали ранее
        max_i = i  # то перезапишем индекс максимального числа
        max_number = current_number  # и перезапишем само текущее число
list_numbers[max_i], list_numbers[-1] = list_numbers[- 1], max_number
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
