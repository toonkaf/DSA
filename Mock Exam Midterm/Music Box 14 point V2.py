"""Queue"""
class Song:
    def __init__(self,name:str,genre:str,durations:int):
        self.name = name
        self.genre = genre
        self.durations = durations
    def show_info(self):
        minute , sec = divmod(self.durations,60)
        return f"{self.name} <|> {self.genre} <|> {minute}.{sec:>02}"

class Queue:
    def __init__(self,count,head):
        self.count = count
        self.head = head
    
    def enqueue(self, )