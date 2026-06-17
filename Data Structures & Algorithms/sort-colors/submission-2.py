class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        r=len(nums)-1
        i=0
        while i<=r:
            if nums[i]==1:
                i=i+1
            elif nums[i]==0:
                temp=nums[i]
                nums[i]=nums[l]
                nums[l]=temp
                l=l+1
                i=i+1
            else:
                temp=nums[i]
                nums[i]=nums[r]
                nums[r]=temp
                r=r-1
                