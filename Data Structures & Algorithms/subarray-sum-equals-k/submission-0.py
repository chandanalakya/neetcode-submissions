class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=[0]*len(nums)
        sum=0
        count=0
        d={}
        for i in range(len(nums)):
            sum=sum+nums[i]
            pre[i]=sum
        for j in range(len(nums)):
            if pre[j]==k:
                count+=1
            if pre[j]-k in d:
                count+=d[pre[j]-k]
            if pre[j] not in d:
                d[pre[j]]=1
            else:
                d[pre[j]]+=1
        return count

            


        
        

