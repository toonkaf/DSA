"""Binary Search Tree (Cases 1, 2, 3)"""
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
            print()
        else:
            print("This is an empty binary search tree.")

    def find_min(self):
        """_"""
        node = self.root
        if node is not None:
            while node.left is not None:
                node = node.left
            return node.data
        else:
            return None
    
    def find_max(self):
        """_"""
        node = self.root
        if node is not None:
            while node.right is not None:
                node = node.right
            return node.data
        else:
            return None

    def delete(self,data):
        """_"""
        def delete_node(node, data):
            if node is None:
                print("Delete Error, %s is not found in Binary Search Tree."%data)
                return None
            if data < node.data:
                node.left = delete_node(node.left, data)
            elif data > node.data:
                node.right = delete_node(node.right, data)
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # else:
                #     successor = node.right
                #     while successor.left is not None:
                #         successor = successor.left
                #     node.data = successor.data
                #     node.right = delete_node(node.right, successor.data)
            return node
        self.root = delete_node(self.root, data)

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()