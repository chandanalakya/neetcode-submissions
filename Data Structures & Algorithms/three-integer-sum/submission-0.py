class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        
        i=0
        a=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue

            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    a.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
                    while l<r and nums[r]==nums[r+1]:
                        r=r-1
                elif nums[i]+nums[l]+nums[r]>0:
                    r=r-1
                else:
                    l=l+1
        return a