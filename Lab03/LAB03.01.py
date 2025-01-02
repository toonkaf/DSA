"""Create Datanode"""
class DataNode:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
    

def main():
    data = input()
    node = DataNode(data)
    print(node.data)
    print(node.next)
main()