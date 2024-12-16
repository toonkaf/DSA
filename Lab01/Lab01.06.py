"""Rectangle"""
class Rectangle:
  def __init__(self, height, width):
    """__"""
    self.height = height
    self.width = width

  def calculate_area(self):
    """area"""
    return self.height * self.width

  def calculate_perimeter(self):
    """perimeter"""
    return self.height*2 + self.width*2


def main(rectangle,condition):
    """main"""
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print(f"{result:.2f}")
main(Rectangle(float(input()), float(input())),input())
