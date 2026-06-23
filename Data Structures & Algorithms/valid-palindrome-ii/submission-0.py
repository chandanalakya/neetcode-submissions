class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l=l+1
                r=r-1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                if ispal(l+1,r) or ispal(l,r-1):
                    return True
                return False
            l=l+1
            r=r-1
        return True