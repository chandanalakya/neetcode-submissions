class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        prefix=[0]*(len(nums)+1)
        suffix=[0]*(len(nums)+1)
        prefix[0]=1
        suffix[-1]=1
        product=1
        p=1
        for i in range(len(nums)):
            product=product*nums[i]
            prefix[i+1]=product
        print(prefix)
        for j in range(len(nums)-1,-1,-1):
            p=p*nums[j]
            suffix[j]=p
        print(suffix)
        for k in range(len(nums)):
            o=prefix[k]*suffix[k+1]
            output[k]=o
        return output



            


