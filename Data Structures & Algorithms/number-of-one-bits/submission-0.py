class Solution:
    def hammingWeight(self, n: int) -> int:
        q=""
        count=0
        while n>0:
            s=n%2
            q=str(s)+q
            n=n//2
        for i in q:
            if i =='1':
                count=count+1
        return count
