"""Seats Number(Bubble Sort)"""
import json
def bubbleSort(lst:list,last:int):
    """___"""
    current = 0
    sortedd = False
    counter = 0
    while current <= last and not sortedd:
        walker = last
        sortedd = True
        while walker > current:
            if lst[walker][0] < lst[walker - 1][0] or (lst[walker][0] == lst[walker - 1][0] and int(lst[walker][1:]) < int(lst[walker - 1][1:])):
                sortedd = False
                lst[walker],lst[walker - 1] = lst[walker - 1],lst[walker]
            counter += 1
            walker -= 1
        print(lst)
        current += 1
    print("Comparison times:",counter)

bubbleSort(json.loads(input()),int(input()))