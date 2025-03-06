"""Knapsack"""
class Item:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.price / self.weight

def knapsack(lst:list,cap: float):
    kept = 0
    prices = 0
    print(f"Knapsack Size: {cap} kg\n===============================")
    lst.sort(key = lambda x: x.get_cost() , reverse=True)
    for i in lst:
        if kept + i.get_weight() <= cap:
            prices += i.get_price()
            kept += i.get_weight()
            print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
    print(f"Total: {prices} THB")
        
    
def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capasity = float(input())
    knapsack(items, knapsack_capasity)
main()