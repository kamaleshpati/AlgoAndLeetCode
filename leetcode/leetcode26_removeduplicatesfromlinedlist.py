from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        counter = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i]:
                nums[counter] = nums[i + 1]
                counter += 1

        return counter
