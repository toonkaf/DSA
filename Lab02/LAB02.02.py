"""Student Groups"""
class ArrayStack :
    def __init__(self,size = 0,data:list = list()):
        self.size = size
        self.data = data
    
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

def main(m: int,n: int):
    """main"""
    stu = ArrayStack(0,list())
    for _ in range(n):
        stu.push(input())
    kept = ArrayStack(0,list())
    kept2 = ArrayStack(0,list())
    for j in range(m,0,-1):
        kept.push(f"Group {j}: ")
    while not stu.is_empty():
        if stu.is_empty():
            break
        for _ in range(m):
            if stu.is_empty():
                break
            x = kept.pop()
            if stu.get_size() <= m:
                x += str(stu.pop())
            else:
                x += str(stu.pop()) + ", "
            kept2.push(x)
        for _ in range(m):
            if kept2.is_empty():
                break
            kept.push(kept2.pop())
    
    for _ in range(m):
        print(kept.pop())

main(int(input()),int(input()))
