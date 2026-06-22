class MyCircularQueue:
    class ListNode:
        def __init__(self,val):
            self.val=val
            self.next=None

    def __init__(self, k: int):
        self.size=k
        self.count=0
        self.head=None
        self.t=None
        

    def enQueue(self, value: int) -> bool:
        
        if self.count==self.size:
            return False
        new=self.ListNode(value)
        if self.count==0:
            self.head=new
            self.t=new
            self.t.next=self.head
            self.count+=1
        else:
            self.t.next=new
            self.t=self.t.next
            self.t.next=self.head
            self.count=self.count+1
        return True

        

    def deQueue(self) -> bool:
        if self.count==0:
            return False
        if self.count==1:
            self.head=None
            self.t=None
            self.count=self.count-1
            return True
        self.head=self.head.next
        self.t.next=self.head
        self.count-=1
        return True

    def Front(self) -> int:
        if self.count==0:
            return -1
        else:
            return self.head.val

    def Rear(self) -> int:
        if self.count==0:
            return -1
        else:
            return self.t.val
        

    def isEmpty(self) -> bool:
        if self.count==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count==self.size:
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