class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            other = self.search(target - nums[i], nums, i)
            if other != -1:
                return [i, other]

    def search(self, target, nums, i):
        for j in range(i + 1, len(nums)):
            if nums[j] == target:
                return j
        return -1


if __name__ == '__main__':
    Solution().twoSum([2, 7, 11, 15], 9)
