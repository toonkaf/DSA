"""Coin Exchange"""

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    want = int(input())
    data = convert_key(json.loads(input()))
    kept = {10:0,5:0,2:0,1:0}
    money = 0
    for _ in range(data[10]):
        if money + 10 > want or kept[10]>=data[10]:
            break
        kept[10] += 1
        money += 10
    for _ in range(data[5]):
        if money + 5 > want or kept[5]>=data[5]:
            break
        kept[5] += 1
        money += 5
    for _ in range(data[2]):
        if money + 2 > want or kept[2]>=data[2]:
            break
        kept[2] += 1
        money += 2
    for _ in range(data[1]):
        if money + 1 > want or kept[1]>=data[1]:
            break
        kept[1] += 1
        money += 1
    if money < want:
        print(f"Amount: {want}")
        print("Coins are not enough.")
    else:
        print(f"Amount: {want}")
        print("Coin exchange result:")
        print(f"  10 baht = {kept[10]} coins\n  5 baht = {kept[5]} coins\n  2 baht = {kept[2]} coins\n  1 baht = {kept[1]} coins")
        print(f"Number of coins: {kept[10]+kept[5]+kept[2]+kept[1]}")


main()