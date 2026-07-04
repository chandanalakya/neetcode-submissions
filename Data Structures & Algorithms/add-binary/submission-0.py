class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b='0'*(len(a)-len(b))+b
        elif len(a)<len(b):
            a='0'*(len(b)-len(a))+a
        l=[]
        c=0
        i=len(a)-1
        j=len(b)-1
        while i>=0 and j>=0:
            s=c+int(a[i])+int(b[j])
            if s==0:
                c=0
                s=0
            if s==1:
                c=0
                s=1
            if s==2:
                c=1
                s=0
            if s==3:
                c=1
                s=1
            l.append(str(s))
            i=i-1
            j=j-1
        if c!=0:
            l.append(str(c))
        
        return "".join(l[::-1])

    
        