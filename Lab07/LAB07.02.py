"""Selection sort"""
import json
def selectionSort(lst: list,last: int):
    current = 0
    counter = 0
    for _ in range(last):
        walker = current +1
        smallest = current
        for _ in range(walker,last+1):
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1
            counter += 1
        lst[smallest],lst[current] = lst[current],lst[smallest]
        print(lst)
        current += 1
    print("Comparison times:",counter)



selectionSort(json.loads(input()),int(input()))