class Solution:
    def gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        o=self.gcd(len(str1),len(str2))
        candidate=str1[:o]
        if candidate*(len(str1)//len(candidate))==str1 and candidate*(len(str2)//len(candidate))==str2:
            return candidate
        else:
            return ""        