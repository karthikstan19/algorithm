#!usr/bin/env python
def binary_search(arr, val):
    first = 0
    last = len(arr) -1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) //2
        if arr[mid] == val:
            index = mid
        else:
            if val < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
print(binary_search([10,20,30,40,50], 40))
