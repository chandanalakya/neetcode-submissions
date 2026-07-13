class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        count=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l=l+1
            count=count+1
            r=r-1
        return count
       
