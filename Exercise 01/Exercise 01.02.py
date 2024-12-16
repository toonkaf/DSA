"""Elevator"""
class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        if floor > self.max_floor:
            print("Invalid Floor!")
        else:
            self.current_floor = floor

    def report_current_floor(self):
        print(self.current_floor)

def main():
    """main"""
    x = int(input())
    ele = Elevator(x)
    while True:
        x = input()
        if x == "Done":
            break
        ele.go_to_floor(int(x))
    ele.report_current_floor()
main()
