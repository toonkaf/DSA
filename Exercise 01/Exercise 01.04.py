"""Laew Tae App V.1"""
class LaewTaeApp:
    """Menu"""
    def __init__(self):
        self.menu = ["Pizza","Fried Chicken","Hamburger","Steak"]
        self.ran = 1
    
    def random_foods(self):
        self.ran += 1
    
    def list_foods(self):
        print(sorted(self.menu))

    def add_food_item(self,name):
        self.menu.append(name)
        

def main(n):
    """main"""
    app = LaewTaeApp()
    for _ in range(n):
        app.add_food_item(input())
    app.list_foods()

main(int(input()))
