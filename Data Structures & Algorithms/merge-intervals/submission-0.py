class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=[]
        intervals.sort(key=lambda x:x[0])
        l.append(intervals[0])
        for i in range(1,len(intervals)):
            h=l[-1]
            u=intervals[i]
            if u[0]<=h[-1] :
                h[1]=max(u[1],h[1])
            else:
                l.append(u)
        return l