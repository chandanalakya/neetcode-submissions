class MinStack:

    def __init__(self):
        self.stack=[]
        self.s=[]
        self.m=float("inf")
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if len(self.s)==0:
            self.s.append(val)
        else:
            self.s.append(min(val,self.s[-1]))
        
        

    def pop(self) -> None:
        x=self.stack.pop()
        self.s.pop()
        return x
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.s[-1]
        
        
