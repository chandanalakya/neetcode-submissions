class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        if len(s)==1:
            return False
        for i in s:
            if i=='['or i=='('or i=='{':
                l.append(i)
            elif i==']':
                if l and l[-1]=='[':
                    l.pop()
                else:
                    return False
            elif i==')':
                if l and l[-1]=='(':
                    l.pop()
                else:
                    return False
            else:
                if l and l[-1]=='{':
                    l.pop()
                else:
                    return False
        if len(l)==0:
            return True
        else:
            return False

            
