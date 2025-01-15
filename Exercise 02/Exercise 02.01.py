"""Infix to Postfix V.1"""
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

def intopost(s: str):
    """Infix to Postfix"""
    kept = ArrayStack()
    res = ""
    c1 = 0
    c2 = 0
    for i in s:
        if i.isalpha():
            res += i
        else:
            if kept.is_empty():
                kept.push(i)
            else:
                if i in ("+","-"):
                    c1 = 1
                else:
                    c1 = 2
                if kept.get_stack_top() in ("+","-"):
                    c2 = 1
                else:
                    c2 = 2
                if c1 > c2:
                    kept.push(i)
                else:
                    while c1 <= c2:
                        res += kept.pop()
                        if kept.is_empty():
                            break
                        if kept.get_stack_top() in ("+","-"):
                            c2 = 1
                        else:
                            c2 = 2
                    kept.push(i)            
    while not kept.is_empty():
        res += kept.pop()
    print(res)

intopost(input().replace(" ",""))