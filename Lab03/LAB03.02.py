"""Singly Linked List (Traversal and Insert Last)"""
class DataNode:
    """_"""
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """_"""
    def __init__(self,count: int=0,head:DataNode = None):
        self.count = count
        self.head = head
    
    def traverse(self):
        """_"""
        n = self.head
        if n is None:
            print("This is an empty list.")
            return
        print(n.data,end=" ")
        n = n.next
        while n is not None:
            print("->",n.data,end=" ")
            n = n.next
        
    def insert_last(self,data:DataNode):
        """_"""
        n = self.head
        if self.head is None:
            self.head = DataNode(data)
            return
        while n is not None:
            if n.next == None:
                n.next = DataNode(data)
                break
            n = n.next

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()
