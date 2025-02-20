"""Insertion sort"""
import json
def insertionSort(lst:list,last):
    current = 1
    count = 0
    for _ in range(last):
        if lst[current] < lst[current - 1]:
            lst[current] , lst[current - 1] = lst[current - 1] , lst[current]
            count += 1
            for i in range(current-1,0,-1):
                count += 1
                if lst[i] >=  lst[i-1]:
                    break
                lst[i],lst[i-1] = lst[i-1],lst[i]
        else:
            count +=1
        print(lst)
        current += 1
    print("Comparison times:",count)


insertionSort(json.loads(input()),int(input()))