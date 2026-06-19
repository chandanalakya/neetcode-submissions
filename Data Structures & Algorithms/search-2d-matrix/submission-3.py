class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        s=len(matrix[0])-1
        a=-1
        while i<len(matrix):
            if matrix[i][0]<=target<=matrix[i][s]:
                a=i
            i=i+1
        l=0
        r=s
        while l<=r:
            mid=(l+r)//2
            if matrix[a][mid]==target:
                return True
            elif matrix[a][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
