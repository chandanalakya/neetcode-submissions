class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        a=set()
        mx=0
        for j in range(len(s)):
            while s[j]  in a:
                a.discard(s[i])
                i=i+1
            a.add(s[j])
            mx=max(mx,j-i+1)

            
        return mx

