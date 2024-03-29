class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.list=[-1]*k
        self.head=0
        self.tail=0
        self.size=0

    def enQueue(self, value: int) -> bool:
        if self.size==self.k:
            return False
        self.list[self.tail%self.k]=value
        self.tail+=1
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.size==0:
            return False
        self.list[self.head%self.k]=-1
        self.head+=1
        self.size-=1
        return True

    def Front(self) -> int:
        return self.list[self.head%self.k]

    def Rear(self) -> int:
        return self.list[(self.tail-1)%self.k]

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()