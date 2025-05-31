class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        l, r = 0, len(nums) - 1
        if (len(nums)==0):
            return 0

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l