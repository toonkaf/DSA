"""Binary Search Tree (Preorder, Insert)"""
class BSTNode:
    """_"""
    def __init__(self,data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """_"""
    def __init__(self,root:BSTNode = None):
        self.root = root
    
    def insert(self,data):
        """_"""
        data = BSTNode(data)
        n = self.root
        if n is None:
            self.root = data
            return
        while True:
            if data.data < n.data :
                if n.left is None:
                    n.left = data
                    break
                n = n.left
            elif data.data >= n.data:
                if n.right is None:
                    n.right = data
                    break
                n = n.right

    def preorder(self,node = None):
        """_"""
        if node is None:
            node = self.root
        if node is not None:
            print("->",node.data,end = " ")
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
        
    print("Preorder: ", end="")
    my_bst.preorder()

main()