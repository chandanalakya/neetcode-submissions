class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        pre=[0]*(len(nums)+1)
        pos=[0]*(len(nums)+1)
        pre[0]=1
        pos[-1]=1
        product=1
        p=1
        for i in range(0,len(nums)):
            p=p*nums[i]
            pre[i+1]=p
        print(pre)
        for j in range(len(nums)-1,-1,-1):
            product=product*nums[j]
            pos[j]=product
        print(pos)
        for i in range(len(output)):
            output[i]=pre[i]*pos[i+1]
        return output
        

