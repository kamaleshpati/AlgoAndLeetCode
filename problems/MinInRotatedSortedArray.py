class MinSortedRotated:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while r > l:
            m = l + (r - l) // 2 

            if nums[r] < nums[m]:
                res = min(res, nums[r])
                l = m + 1
            elif nums[r] > nums[m]:
                r = m
            else:
                r -= 1

        res = min(res, nums[l])
        return res
