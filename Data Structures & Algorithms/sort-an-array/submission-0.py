class Solution:

    def merge(self, nums, l, mid, r):
        left = nums[l:mid+1]
        right = nums[mid+1:r+1]

        i = 0
        j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def mergesort(self, nums, l, r):
        if l >= r:
            return

        mid = (l + r) // 2

        self.mergesort(nums, l, mid)
        self.mergesort(nums, mid + 1, r)

        self.merge(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums