class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0
        while j<len(nums):
            if nums[j]!=val:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i=i+1
            j=j+1
        return i