from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        while left< right:
            current = (right-left) * min(height[left],height[right])
            if height[left]<height[right]:
                left += 1
            else:
                right -=1
            res = max(current,res)
        return res