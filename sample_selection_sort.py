#!usr/bin/env python
#Selection sort
def selection_sort(number):
    for i in range(len(number)):
        minimum = i
        for j in range(i+1,len(number)):
            if number[j] < number[minimum]:
                minimum = j

        number[minimum], number[i] = number[i], number[minimum]

    return number
number = [10, 60, 30, 20, 80, 70]
result = selection_sort(number)
print(result)
#output = [10, 20, 30, 60, 70, 80]

