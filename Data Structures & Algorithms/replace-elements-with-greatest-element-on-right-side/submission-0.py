class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=0
        while i<len(arr)-1:
            j=i+1
            mx=0
            while j<len(arr):
                if arr[j]>mx:
                    mx=arr[j]
                j=j+1
            arr[i]=mx
            i=i+1
        arr[-1]=-1
        return arr
