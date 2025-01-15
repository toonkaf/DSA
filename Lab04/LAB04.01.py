"""Create BSTNode"""
class BSTNode:
    """_"""
    def __init__(self,data: int = None):
        self.data = data
        self.left = None
        self.right = None

def main():
    """main"""
    b = BSTNode(int(input()))
    print(b.data)
    print(b.left)
    print(b.right)

main()
