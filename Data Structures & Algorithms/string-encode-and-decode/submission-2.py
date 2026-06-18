class Solution:

    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
            s.append(str(len(i)))
            s.append('#')
            s.append(i)
        return "".join(s)
    def decode(self, s: str) -> List[str]:
        i=0
        le=""
        l=[]
        d=''
        while i<len(s):
            le=""
            while s[i]!='#':
                le=le+s[i]
                d=''
                i=i+1
            i=i+1
            count=int(le)
            while count>0:
                d=d+s[i]
                i=i+1
                count=count-1
            l.append(d)
        return l
        

