class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix[0])-1
        i=0
        while i<len(matrix):
            l=0
            r=len(matrix[0])-1
            while l<=r:
                mid=(l+r)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            i=i+1
        return False
