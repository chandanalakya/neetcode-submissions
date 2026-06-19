class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t=0
        u=len(matrix)-1
        a=-1
        while t<=u:
            m=(t+u)//2
            if matrix[m][0]<=target<=matrix[m][-1]:
                a=m
                break
            elif target>matrix[m][-1]:
                t=m+1
            elif target<matrix[m][0]:
                u=m-1
        if a==-1:
            return False
        l=0
        r=len(matrix[0])-1
        while l<=r:
            mid=(l+r)//2
            if matrix[a][mid]==target:
                return True
            elif matrix[a][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
