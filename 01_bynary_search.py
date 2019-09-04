# Бинарный поиск
def binary_search(list, item):      # в первый аргумент передается массив в котором нужно выполнить
                                    # поиск, а во второй элемент который нужно найти
    low = 0                         # крайний наименьший элемент
    high = len(list) - 1            # крайний наибольший элемент

    while low <= high:              # пока эта чать не сократиться до одного элемента
        mid = (low + high) // 2     # провереяем средний элемент
        guess = list[mid]

        if guess == item:           # значение найдено
            return mid
        if guess > item:            # много
            high = mid - 1
        else:                       # мало
            low = mid + 1
    return None                     # Значения не существет

my_list = [1, 3, 5, 7, 9]           # тестируем

print(binary_search(my_list, 5))    # Вернет 2 так как 5 это элемент под индексом 2
print(binary_search(my_list, 6))    # Вернет None так как значения нет в массиве
print(binary_search(my_list, -1))   # Вернет None так как значения нет в массиве