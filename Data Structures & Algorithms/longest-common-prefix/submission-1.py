class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        
        if len(strs)==1:
            return strs[0]


        a=set()
        while i<len(strs)-1:
            j=0
            s=""
            while j<len(min(strs,key=len)):
                if strs[i][j]==strs[i+1][j]:
                    s=s+strs[i][j]
                else:
                    break
                j=j+1
            a.add(s)
            i=i+1
        return min(a,key=len)

            
            
