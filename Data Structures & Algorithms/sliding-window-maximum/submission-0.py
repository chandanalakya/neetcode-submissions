class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        a = []

        for j in range(len(nums)):
            if j - i + 1 == k:
                mx = max(nums[i:j+1])
                a.append(mx)
                i += 1

        return a