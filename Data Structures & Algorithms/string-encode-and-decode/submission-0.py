class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+i+";"
        return s

    def decode(self, s: str) -> List[str]:
        d=""
        i=0
        l=[]
        while i<len(s):
            if s[i]!=';':
                d=d+s[i]
            else:
                l.append(d)
                d=""
            i=i+1
        return l



