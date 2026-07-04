class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        l=[]
        d = {i: chr(64 + i) for i in range(1, 27)}
        while columnNumber>0:
            s=(columnNumber-1)%26
            columnNumber=(columnNumber-1)//26
            l.append(d[s+1])
        return "".join(l[::-1])

        