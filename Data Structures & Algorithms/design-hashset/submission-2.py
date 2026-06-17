class MyHashSet:

    def __init__(self):
        self.a=[0]*1000001

    def add(self, key: int) -> None:
            self.a[key]=key
        

    def remove(self, key: int) -> None:
        self.a[key]=0
        

    def contains(self, key: int) -> bool:
        if self.a[key]!=0:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)