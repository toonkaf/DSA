"""KnapsackV2"""
import json
def knap(itemList: list,amount: int):
    """_"""
    n = len(itemList)
    cell = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    selected = [[[] for _ in range(amount + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name = itemList[i-1][0]
        item_price = itemList[i-1][1]
        item_weight = itemList[i-1][2]
        
        for w in range(amount + 1):
            if item_weight > w:
                cell[i][w] = cell[i-1][w]
                selected[i][w] = selected[i-1][w]
            else:
                if cell[i-1][w] > cell[i-1][w-item_weight] + item_price:
                    cell[i][w] = cell[i-1][w]
                    selected[i][w] = selected[i-1][w]
                else:
                    cell[i][w] = cell[i-1][w-item_weight] + item_price
                    selected[i][w] = selected[i-1][w-item_weight] + [i-1]
    
    selected_i = selected[n][amount]
    tt_price = cell[n][amount]
    
    res = {}
    for k in selected_i:
        res[itemList[k][0]] = [itemList[k][1],itemList[k][2]]
    sorts = sorted(res.keys())
    print(f"Total: {tt_price}")
    for i in sorts:
        print(f"{i} -> {res[i][1]} kg -> {res[i][0]} THB")
    
knap(json.loads(input()),int(input()))