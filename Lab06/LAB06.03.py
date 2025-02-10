"""Binary Search"""
import json
class Student:
    def __init__(self,std_id: int,name:str,gpa: float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    
    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return self.gpa

    def print_details(self):
        print(f"ID: {self.std_id}\nName: {self.name}\nGPA: {self.gpa:.2f} ")

def binary_search(data: list,name: str):
    """BS"""
    check = True
    start = 0
    end = len(data) - 1
    count = 0
    while check:
        mid = int((start + end) / 2)
        count += 1
        if start == end:
            check = False
        if name == data[mid].get_name():
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {count}")
            return
        elif name[0] == data[mid].get_name()[0]:
            for i,j in enumerate(name):
                if j > data[mid].get_name()[i]:
                    start = mid + 1
                    break
                elif j < data[mid].get_name()[i]:
                    end = mid - 1
                    break
        elif name[0] > data[mid].get_name()[0]:
            start = mid + 1
        elif name[0] < data[mid].get_name()[0]:
            end = mid - 1
    print(f"{name} does not exists.")
    print(f"Comparisons times: {count}")

                
                
    
    
    
    
    
    
    
def main():
    """main"""
    raw = json.loads(input())
    data = list()
    for i in raw:
        data.append(Student(i["id"], i["name"], i["gpa"]))
    binary_search(data,input())
main()
        
    