class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z = 0       # Count of zeros in current window
        res = 0     # Max length of valid window
        l = 0       # Left pointer of the window

        for i in range(len(nums)):
            # If current element is 0, increment zero counter
            if nums[i] == 0:
                z += 1
                
            # If window is valid (has at most k zeros), update result
            if z <= k:
                res = max(res, i - l + 1)

            # If window has too many zeros, shrink from left
            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1

        return res