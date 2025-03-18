"""Card Sorting (Easy)"""
import json
kept = ["KS","QS","JS","10S","9S","8S","7S","6S","5S","4S","3S","2S","1S","AS",
        "KH","QH","JH","10H","9H","8H","7H","6H","5H","4H","3H","2H","1H","AH",
        "KD","QD","JD","10D","9D","8D","7D","6D","5D","4D","3D","2D","1D","AD",
        "KC","QC","JC","10C","9C","8C","7C","6C","5C","4C","3C","2C","1C","AC"]
kept2 = {c:i for i, c in enumerate(kept)}
def bubble(target):
    """---"""
    k = len(target)
    for i in range(k):
        for j in range(k - 1):
            if kept2[target[j]] > kept2[target[j+ 1]]:
                target[j], target[j+1] = target[j+1] , target[j]
    return target

def bubble2(lst:list,last:int):
    """___"""
    current = 0
    sortedd = False
    counter = 0
    while current <= last and not sortedd:
        walker = last
        sortedd = True
        while walker > current:
            if lst[walker] < lst[walker - 1]:
                sortedd = False
                lst[walker],lst[walker - 1] = lst[walker - 1],lst[walker]
            walker -= 1
        current += 1
    return lst
def bubble3(lst:list,last:int,dic: dict):
    """___"""
    current = 0
    sortedd = False
    counter = 0
    while current <= last and not sortedd:
        walker = last
        sortedd = True
        while walker > current:
            if dic[lst[walker]][0] < dic[lst[walker - 1]][0]:
                sortedd = False
                lst[walker],lst[walker - 1] = lst[walker - 1],lst[walker]
            walker -= 1
        current += 1
    return lst
def card(n,m):
    """---"""
    people = {}
    name = []
    for i in range(n):
        x = json.loads(input())
        score = 0
        for i in x[1]:
            if i in ("2C","QS"):
                score += 50
            elif "A" in i[0]:
                score += 15
            elif "10" in i[:2] or i[0] in ("J","Q","K"):
                score += 10
            else:
                score += 5
        people[x[0]] = [score,bubble(x[1])]
        name.append(x[0])
    name = bubble2(name,len(name)-1)
    name = bubble3(name,len(name)-1,people)
    name.reverse()
    for i in name:
        print(f"{i} -> {people[i][0]} -> {people[i][1]}")

card(int(input()),int(input()))