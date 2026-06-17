class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            d={}
            l={}
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]]+=1
                else:
                    d.update({s[i]:1})
                if t[i] in l:
                    l[t[i]]+=1
                else:
                    l.update({t[i]:1})
        if d==l:
            return True
        else:
            return False