from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
        return count

if __name__ == '__main__':
    li = [0,1,2,2,3,0,4,2]
    print(Solution().removeElement(li,2))
    print(li)



