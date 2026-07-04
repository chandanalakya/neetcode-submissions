class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0]
        for i in range(1,n+1):
            l1=[]
            while i>0:
                d=i%2
                c=i//2
                i=i//2
                l1.append(str(d))
            a=l1.count('1')
            l.append(a)
        return l
