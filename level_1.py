def binary_search_recursive(a,search_item):
    low = 0
    high = len(a) - 1
    middle = (low + high)//2
    return recursive(a, low, high, middle, search_item)

def recursive(a,low,high,middle,search_item):
    middle = (low + high)//2
    if a[middle]==search_item:
        return True
    if a[middle] > search_item:
         high = middle - 1
    else:
         low = middle + 1
    if low < high:
        return recursive(a, low, high, middle, search_item)
    return False


def binary_search(list, goal):
    mid = len(list) // 2
    low = 0
    high = len(list) - 1
    
    while list[mid] != goal and low <= high:
        if goal > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    if low > high:
        return False
    return True


a=[2,6,20,25,32,40]
value = 64
result = binary_search_recursive(a,value)
if result:
    print('binary_search_recursive: Элемент найден')
else:
    print('binary_search_recursive: Элемент не найден')

result = binary_search(a, value)
if result:
    print('binary_search: Элемент найден')
else:
    print('binary_search: Элемент не найден')