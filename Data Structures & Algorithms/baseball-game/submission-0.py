class Solution:
    def calPoints(self, ops: List[str]) -> int:
        a=[]
        for i in range(len(ops)):
            if ops[i]=='+':
                l=a[-1]+a[-2]
                a.append(l)
            elif ops[i]=='D':
                l=2*a[-1]
                a.append(l)
            elif ops[i]=='C':
                a.pop()
            else:
                p=int(ops[i])
                a.append(p)
        print(a)
        return sum(a)

                