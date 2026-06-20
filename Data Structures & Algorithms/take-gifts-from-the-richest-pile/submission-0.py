import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k>0:
            a=max(gifts)
            w=gifts.index(a)
            gifts[w]=math.isqrt(a)
            k=k-1
        print(gifts)
        return sum(gifts)



        
