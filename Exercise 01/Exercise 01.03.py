"""Laew Tae App V.1"""
class LaewTaeApp:
    """Menu"""
    def __init__(self,menu = ["Pizza","Fried Chicken","Hamburger","Steak"],ran = 1):
        self.menu = menu
        self.ran = ran
    
    def random_foods(self):
        self.ran += 1
    
    def list_foods(self):
        print(sorted(self.menu))

LaewTaeApp().list_foods()
