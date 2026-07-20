class Solution:
    def isvalid(self,nums,k,mid):
        p=0
        st=1
        for i in range(len(nums)):
            if (nums[i]+p)<=mid:
                p+=nums[i]
            else:
                st+=1
                p=nums[i]
        if st>k:
            return False
        else:
            return True

    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        while l<=r:
            mid=(l+r)//2
            if self.isvalid(nums,k,mid):
                r=mid-1
            else:
                l=mid+1
        return l

