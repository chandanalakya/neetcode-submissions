class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)
        s = 0
        r = b[::-1]

        for bit in r:
            s = s * 2 + int(bit)
        return s