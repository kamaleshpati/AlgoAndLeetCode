from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]



if __name__ == '__main__':
    li = [3,3,4]
    print(Solution().twoSum(li, 6))
