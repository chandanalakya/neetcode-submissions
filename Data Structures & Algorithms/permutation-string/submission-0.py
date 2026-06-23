from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        s1c=Counter(s1)
        win=Counter()
        k=len(s1)
        for j in range(len(s2)):
            win[s2[j]]+=1
            if j-i+1==k:
                if win==s1c:
                    return True
                win[s2[i]]-=1
                if win[s2[i]]==0:
                    del win[s2[i]]
                i=i+1
        return False