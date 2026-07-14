class Solution:
    def decodeString(self, s: str) -> str:
        w=[]
        
        for i in s:
            z=""
            a=""
            if i!=']':
                w.append(i)
            else:
                while w and w[-1]!='[':
                    a=w.pop()+a
                w.pop()
                while w and w[-1].isdigit():
                    z=w.pop()+z
                a=a*int(z)
                w.append(a)
        return "".join(w)


