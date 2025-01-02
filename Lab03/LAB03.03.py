"""Singly Linked List (Insert Front)"""
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
            self.head = data
            return
        while n is not None:
            if n.next is None:
                n.next = data
                break
            n = n.next
    
    def insert_front(self,data:DataNode):
        """_"""
        n = self.head
        if n is None:
            self.head = data
        else:
            data.next = n
            self.head = data

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(DataNode(data))
        elif condition == "L":
            mylist.insert_last(DataNode(data))
        # elif condition == "B":
        #     mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()