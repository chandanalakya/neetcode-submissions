class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        p=[]
        for i in asteroids:
            if i>0:
                s.append(i)
            else:
                while s and s[-1] > 0:
                    if abs(i)==s[-1]:
                        s.pop()
                        break
                    elif abs(i)>s[-1]:
                        s.pop()
                        continue
                    else:
                        break
                else:
                    s.append(i)
        return s