"""Queue Class"""
class Song:
    """_"""
    def __init__(self,name:str,genre:str,durations:int,next = None):
        self.name = name
        self.genre = genre
        self.durations = int(durations)
        self.next:Song = next
    def show_info(self):
        """_"""
        minute , sec = divmod(self.durations,60)
        print(f"{self.name} <|> {self.genre} <|> {minute}.{sec:>02}")
    def re_info(self):
        minute , sec = divmod(self.durations,60)
        return f"{self.name} <|> {self.genre} <|> {minute}.{sec:>02}"


class Queue:
    """_"""
    def __init__(self,count:int=0,head:Song=None):
        self.count = count
        self.head = head
    def enqueue(self, song:Song):
        """_"""
        n = self.head
        if self.head is None:
            self.head = song
            self.count += 1
            return
        while n is not None:
            if n.next is None:
                n.next = song
                self.count += 1
                return
            n = n.next
    def dequeue(self):
        n = self.head
        if n is None:
            print("Underflow! Dequeue from an empty queue")
            return
        x = self.head
        self.head = n.next
        self.count -= 1
        print("Dequeue item:",end =" ")
        return x
    def peek(self):
        n = self.head
        if n is None:
            print("Underflow! peek from an empty queue")
            return
        print("Peek item:",end=" ")
        return self.head
    def isEmpty(self):
        return not bool(self.count)
    def show_Queue(self):
        n = self.head
        counts = 1
        if n is None:
            print("Queue is empty!")
            return
        while n is not None:
            print(f"Queue#{counts}",n.re_info())
            n = n.next
            counts += 1
            if counts > self.count:
                return
    def lastSong(self,timer: int):
        n = self.head
        counts = 1
        if n is None:
            print("Nothing here! Please add some song")
            return
        while timer > 0:
            timer -= n.durations
            if timer <= 0 :
                print(f"Queue#{counts}",n.re_info())
                return
            if n.next is None:
                n = self.head
                counts = 1
            else:
                n = n.next
                counts += 1
    def removeSong(self,name: str):
        n = self.head
        if n is None:
            print(f"Can not Delete! {name} is not exist")
            return
        if self.head.name == name:
            self.head = self.head.next
            self.count -= 1
            return
        if n.next is None:
            print(f"Can not Delete! {name} is not exist")
            return
        while n.next.name != name:
            if n.next.next is None:
                print(f"Can not Delete! {name} is not exist")
                return
            n = n.next
        n.next = n.next.next
        self.count -= 1
    def groupSong(self):
        k,j,r = "","",""
        n = self.head
        if n is None:
            print("Nothing here! Please add some song")
            return
        while n is not None:
            if n.genre == "KPOP":
                if not k:
                    k = f"KPOP: {n.name}"
                else:
                    k += f" | {n.name}"
            elif n.genre == "JPOP":
                if not k:
                    j = f"JPOP: {n.name}"
                else:
                    j += f" | {n.name}"
            elif n.genre == "R&B":
                if not k:
                    r = f"R&B: {n.name}"
                else:
                    r += f" | {n.name}"
            n = n.next
        print(j,k,r,sep="\n")
    def undo(self):
        pass
    def rev_queue(self):
        pass
    

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp = q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()