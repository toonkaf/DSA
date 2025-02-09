"""ProbHash Hashing"""
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

class ProbHash:
    def __init__(self,size=0):
        self.hash_table = ["" for _ in range(size)]
        self.size = size
    
    def hash(self,key:int):
        key = key % self.size
        if self.hash_table[key]:
            key = self.rehash(key)
            return key
        else:
            return key
            
    def rehash(self,key):
        key += 1
        if key >= self.size and not "" in self.hash_table:
            return key
        if key >= self.size and "" in self.hash_table:
            key = 0
        if self.hash_table[key]:
            key = self.rehash(key)
            return key
        else:
            return key
    
    def insert_data(self,std:Student):
        key = self.hash(std.get_std_id())
        if key >= self.size:
            print(f"The list is full. {std.get_std_id()} could not be inserted.")
            return
        self.hash_table[key] = std
        print(f"Insert {std.get_std_id()} at index {key}")
        return

    def search_data(self,std_id):
        key = std_id % self.size
        kept = key
        once = False
        while True:
            if key >= self.size or (once and key >= kept):
                break
            stu:Student = self.hash_table[key]
            if stu != "":
                if stu.get_std_id() == std_id:
                    print(f"Found {std_id} at index {key}")
                    return stu
            key += 1
            if key >= self.size and not once:
                key = 0
                once = True
        print(f"{std_id} does not exist.")
        return None
                
        
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
        
        