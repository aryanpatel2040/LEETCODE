class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Height is the smaller of the two lines
            h = min(height[left], height[right])
            # Width is the distance between the lines
            w = right - left
            # Update max_area if needed
            max_area = max(max_area, h * w)

            # Move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area