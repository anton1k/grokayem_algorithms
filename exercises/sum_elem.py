def le(arr):
    total = 0
    if arr == []:
        return total
    
    return 1 + le(arr[1:])

print(le([1,2,3,4,5]))