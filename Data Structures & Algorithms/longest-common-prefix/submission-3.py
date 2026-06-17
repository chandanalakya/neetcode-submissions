class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=[]
        for j in range(len(min(strs,key=len))):
            for k in range(1,len(strs)):
                if strs[k][j]!=strs[0][j]:
                    return "".join(p)
            p.append(strs[0][j])
        return "".join(p)
        

