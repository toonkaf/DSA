"""Parentheses Matching"""
class ArrayStack :
    def __init__(self):
        self.size = 0
        self.data = list()
    
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    
    def pop(self):
        """pop"""
        if self.size:
            x = self.data.pop()
            self.size -= 1
        else:
            print("Underflow: Cannot pop data from an empty list")
            x = None
        return x
    
    def is_empty(self):
        """isem"""
        if self.size:
            x = False
        else:
            x = True
        return x
    
    def get_stack_top(self):
        """getst"""
        if self.size:
            x = self.data.pop()
            self.data.append(x)
        else:
            print("Underflow: Cannot get stack top from an empty list")
            x = None
        return x
    
    def get_size(self):
        """gets"""
        return self.size
    
    def print_stack(self):
        """print"""
        print(self.data)

def is_parentheses_matching(expression):
    stack = ArrayStack()
    check = True
    for i in expression:
        if i == '(':
            stack.push(i)
        elif i == ')':
                if stack.pop() == None:
                    check = False
    if check and stack.is_empty():
        print(f"Parentheses in {expression} are matched")
        print("True")
    else:
        print(f"Parentheses in {expression} are unmatched")
        print("False")

is_parentheses_matching(input())