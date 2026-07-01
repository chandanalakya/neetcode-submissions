class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = []
        nums.sort()

        i = 0
        while i < len(nums) - 3:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            while j < len(nums) - 2:

                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                k = j + 1
                r = len(nums) - 1

                while k < r:
                    su = nums[i] + nums[j] + nums[k] + nums[r]

                    if su == target:
                        d.append([nums[i], nums[j], nums[k], nums[r]])
                        k += 1
                        r -= 1

                        while k < r and nums[k] == nums[k - 1]:
                            k += 1

                        while k < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif su > target:
                        r -= 1
                    else:
                        k += 1

                j += 1

            i += 1

        return d