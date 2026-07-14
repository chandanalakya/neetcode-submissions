class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in range(len(tokens)):
            if tokens[i] not in {"+","-","/","*"}:
                s.append(tokens[i])
            else:
                a=s.pop()
                b=s.pop()
                if tokens[i]=="+":
                    c=int(a)+int(b)
                    s.append(c)
                elif tokens[i]=="-":
                    c=int(b)-int(a)
                    s.append(c)
                elif tokens[i]=="*":
                    c=int(a)*int(b)
                    s.append(c)
                else:
                    c=int(int(b)/int(a))
                    s.append(c)
        if len(s)==1:
            x=s.pop()
        return int(x)

        