"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        l=[]
        intervals.sort(key=lambda x:x.start)
        l.append(intervals[0])
        for j in range(1,len(intervals)):
            h=l[-1]
            u=intervals[j]
            if u.start<h.end:
                return False
            else:
                l.append(u)
        return True
