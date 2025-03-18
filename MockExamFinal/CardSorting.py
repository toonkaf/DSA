"""Card Sorting (Easy)"""
import json
kept = ["KS","QS","JS","10S","9S","8S","7S","6S","5S","4S","3S","2S","1S","AS",
        "KH","QH","JH","10H","9H","8H","7H","6H","5H","4H","3H","2H","1H","AH",
        "KD","QD","JD","10D","9D","8D","7D","6D","5D","4D","3D","2D","1D","AD",
        "KC","QC","JC","10C","9C","8C","7C","6C","5C","4C","3C","2C","1C","AC"]
# print(sorted(["5H", "1S", "KC", "7S"],key= lambda x: kept.index(x)))
def cardsorted(n,m):
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
        people[x[0]] = [score,sorted(x[1],key = lambda x: kept.index(x))]
        name.append(x[0])
    name.sort(reverse=True)
    name.sort(key= lambda x:people[x][0] ,reverse=True)
    for i in name:
        print(f"{i} -> {people[i][0]} -> {people[i][1]}")

cardsorted(int(input()),int(input()))







