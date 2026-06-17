class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        a=[]
        c=[]
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        while d!={}:
            key=max(d,key=d.get)
            a.append(key)
            del d[key]
        for j in range(0,k):
            c.append(a[j])
        return c

        