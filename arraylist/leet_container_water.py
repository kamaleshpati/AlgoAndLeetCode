class Solution:
    def maxArea(self, height: []) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            current = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            res = max(current, res)
        return res


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
