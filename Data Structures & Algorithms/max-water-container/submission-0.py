class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        mx=0
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            area=width*height
            if area>mx:
                mx=area
            if heights[i]<heights[j]:
                i=i+1
            else:
                j=j-1
        return mx
            

        

    