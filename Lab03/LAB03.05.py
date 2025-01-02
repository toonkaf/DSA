"""Singly Linked List (Delete)"""
class DataNode:
    """_"""
    def __init__(self,data=None):
        self.data = data
        self.next:DataNode = None

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
        data = DataNode(data)
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
        data = DataNode(data)
        if n is None:
            self.head = data
        else:
            data.next = n
            self.head = data

    def insert_before(self,node,data: DataNode):
        """_"""
        n = self.head
        data = DataNode(data)
        if n is None:
            print("Cannot insert, %s does not exist." %node)
        else:
            if n.data == node:
                data.next = self.head
                self.head = data
            else:    
                while n.data != node:
                    m = n
                    n = n.next
                    if n is None and m.data != node:
                        print("Cannot insert, %s does not exist."%node)
                        return
                data.next = n
                m.next = data

    def delete(self,data):
        """_"""
        n = self.head
        if n is None:
            print("Cannot delete, %s does not exist."%data)
            return
        if n.data == data:
            self.head = n.next
            return
        while n.next is not None and n.next.data != data:
            n = n.next
            if n.next is None:
                print("Cannot delete, %s does not exist." % data)
                return
        n.next = n.next.next


def main():
    """_"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main() 