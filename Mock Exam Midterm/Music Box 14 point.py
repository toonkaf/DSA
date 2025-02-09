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
        return (f"{self.name} <|> {self.genre} <|> {minute}.{sec:>02}")
class Queue:
    """_"""
    def __init__(self,count:int=0,head:Song=None):
        self.count = count
        self.head = head
        self.duration = 0
    def enqueue(self, song:Song):
        """_"""
        n = self.head
        if self.head is None:
            self.head = song
            self.count += 1
            self.duration += song.durations
            return
        while n is not None:
            if n.next is None:
                n.next = song
                self.count += 1
                self.duration += song.durations
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
        self.duration -= x.durations
        return x
    def peek(self):
        n = self.head
        if n is None:
            print("Underflow! peek from an empty queue")
            return
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
            print(f"Queue#{counts}",n.show_info())
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
        timer = timer % self.duration
        while timer >= 0:
            timer -= n.durations
            if timer < 0 :
                print(f"Queue#{counts}",n.show_info())
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
    

def main(): #อธิบายโค้ดในส่วนของ main()
    """this is main function"""
    q = Queue() #สร้าง Queue ว่างขึ้นมา
    while (choice := input()) != "End": #ลูปรับค่าไปเรื่อย ๆ จนกว่าจะเจอคำว่า End
        command, data = choice.split(": ") #แยก input ออกเป็น 2 ค่า คือ command ในการเรียกใช้แต่ละ methods และ data สำหรับใส่เป็น Arguments ของ methods นั้น ๆ ( ถ้ามี )
        match command: # ใช้ match-case เพื่อจับคู่คำสั่งการทำงาน
            case "enqueue":
                q.enqueue(Song(*data.split("|")))  # เพิ่ม object ที่สร้างจากคลาส Song เข้าไปที่ส่วนท้ายของคิว
            case "dequeue":
                temp = q.dequeue() # ทำการลบและคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp: # ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Dequeue item:", temp.show_info())
            case "peek":
                temp= q.peek() # ทำการคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp:# ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Peek item:", temp.show_info())
            case "isEmpty":  # เรียกใช้ isEmpty เพื่อดูว่าคิวว่างหรือไม่
                print(q.isEmpty())
            case "showQueue": # เรียกใช้ showQueue เพื่อแสดงผลข้อมูลเพลงในคิวตามลำดับ
                q.show_Queue()
            case "lastSong":  # เรียกใช้ lastSong เพื่อดูข้อมูลเพลงสุดท้ายที่จะได้ฟัง
                q.lastSong(int(data))
            case "removeSong": # เรียกใช้ removeSong เพื่อลบเพลงนั้นๆ ออกจากคิว
                q.removeSong(data)
            case "groupSong": # เรียกใช้ groupSong เพื่อแสดงชื่อเพลงตามประเภทของเพลง
                q.groupSong()
            case "undo": # เรียกใช้ undo เพื่อย้อนคืนการทำงาน
                q.undo()
            case "rev": # เรียกใช้ rev ย้อนกลับลำดับของเพลงในคิว
                q.rev_queue()
    q.show_Queue() # แสดงข้อมูลเพลงในคิว ก่อนจะจบการทำงานของฟังก์ชัน
main()
