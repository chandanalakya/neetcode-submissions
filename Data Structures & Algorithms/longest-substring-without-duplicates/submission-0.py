class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0

        for i in range(len(s)):
            o = set()

            for j in range(i, len(s)):
                if s[j] in o:
                    break

                o.add(s[j])
                mx = max(mx, j - i + 1)

        return mx