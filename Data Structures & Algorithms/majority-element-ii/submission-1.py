class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1=None
        cand2=None
        count1=0
        count2=0
        c1=0
        c2=0
        n=len(nums)
        for i in nums:
            if i==cand1:
                count1+=1
            elif i==cand2:
                count2+=1
            elif count1==0:
                cand1=i
                count1=1
            elif count2==0:
                cand2=i
                count2=1
            else:
                count1-=1
                count2-=1
        for i in nums:
            if i==cand1:
                c1=c1+1
            elif i==cand2:
                c2=c2+1
        if c1>n//3 and c2>n//3:
            return [cand1,cand2]
        elif c1>n//3 and c2<=n//3:
            return [cand1]
        elif c1<=n//3 and c2>n//3:
            return [cand2]
        else:
            return []
        

        

