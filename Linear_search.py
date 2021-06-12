#!usr/bin/env python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [99, 67, 87, 11, 45, 21]
x = 11
# call function
result = linear_search(arr, x)
if ( result == -1 ):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

# OUTPUT : Element is present at index 3
