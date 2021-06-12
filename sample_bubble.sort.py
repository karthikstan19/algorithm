#!usr/bin/env python
#Bubble sort
def bubble_sort(number):
    swap = True
    while swap:
        swap = False
        for i in range(len(number)-1):
            if number[i] > number[i + 1]:
                number[i], number[i + 1] = number[i + 1] , number[i]
                swap = True
random_list = [5, 2, 1, 8, 4]
bubble_sort(random_list)
print(random_list)
#output = [1, 2, 4, 5, 8]


