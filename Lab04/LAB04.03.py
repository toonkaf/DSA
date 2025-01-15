"""Binary Search Tree (Traversals)"""
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
        if  node is not None:
            print("->",node.data,end = " ")
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def is_empty(self,node = None):
        """_"""
        return not bool(self.root)

    def inorder(self,node = None):
        """_"""
        if node is None:
            node = self.root
        if  node is not None:
            if node.left:
                self.inorder(node.left)
            print("->",node.data,end = " ")
            if node.right:
                self.inorder(node.right)

    def postorder(self,node = None):
        """_"""
        if node is None:
            node = self.root
        if  node is not None:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print("->",node.data,end = " ")
    
    def traverse(self):
        """_"""
        if not self.is_empty():
            print("Preorder:",end=" ")
            self.preorder()
            print()
            print("Inorder:",end=" ")
            self.inorder()
            print()
            print("Postorder:",end=" ")
            self.postorder()
        else:
            print("This is an empty binary search tree.")

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()