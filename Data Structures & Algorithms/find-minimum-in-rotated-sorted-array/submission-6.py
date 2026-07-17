class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= nums[l]:
                # Left half is sorted
                if nums[mid] > nums[r]:
                    l = mid + 1      # Minimum is in the right half
                else:
                    return nums[l]   # Entire search space is sorted
            else:
                # Rotation is in the left half
                r = mid              # Keep mid because it could be the minimum

        return nums[l]