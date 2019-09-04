# Сортировка выбором
def findSmallest(arr, flag):
    smallest = arr[0]                           # для хранения значения
    smallest_index = 0                          # для хранения индекса значения

    for i in range(1, len(arr)):
        if flag == '<':
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        else:
            if arr[i] > smallest:
                smallest = arr[i]
                smallest_index = i
    
    return smallest_index

def selectionSort(arr, flag):                    # сортирует массив
    '''flag указывает в какую сторону сортировать массив'''
    newArr =[]

    for i in range(len(arr)):                    # Находит наименьший элемент в массиве
        smallest = findSmallest(arr, flag)       # и добавляет его в новый массив
        newArr.append(arr.pop(smallest))

    return newArr

print(selectionSort([5, 3, 6, 2, 10], '<'))      # выведет отсортированный массив в порядке 
                                                 # возрастания
print(selectionSort([5, 3, 6, 2, 10], '>'))      # выведет отсортированный массив в порядке 
                                                 # убывания