def quicksort(array):
    if len(array) < 2:                                  # Базовый случайЖ массивы с 0 и 1 элементом
        return array                                    # уже "отсортированы"
    else:
        pivot = array[0]                                # Рекрусивный случай
        less = [i for i in array[1:] if i <= pivot]     # подмассив всех элементов, меньше опорного

        greater = [i for i in array[1:] if i > pivot]   # подмассив всех элементов, больше опорного

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))