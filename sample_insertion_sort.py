#!usr/bin/env python
#insertion sort
def insertion_sort(num):
    for i in range(len(num)):
        cursor = num[i]
        position = i
        while position > 0 and num[position - 1] > cursor:
            num[position] = num[position - 1]
            position = position - 1
        num[position] = cursor
    return num

num = [7, 3, 9, 1 , 6]
result = insertion_sort(num)
print(result)
#output [1, 3, 6, 7, 9]
