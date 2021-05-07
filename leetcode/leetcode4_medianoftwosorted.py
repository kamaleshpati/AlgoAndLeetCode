from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        len1 = len(nums1)
        len2 = len(nums2)
        arr = self.mergeArrays(nums1,nums2,len1,len2)
        return self.median(arr, len2+len1)

    def mergeArrays(self, arr1, arr2, n1, n2):
        arr3 = [None] * (n1 + n2)
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr3[k] = arr1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = arr2[j]
                k = k + 1
                j = j + 1
        while i < n1:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        while j < n2:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
        return arr3

    def median(self, arr, n):
        if n % 2 == 0:
            return (arr[int(n / 2)] + arr[int(n / 2) - 1]) / 2
        else:
            return arr[int(n / 2)]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    Solution().findMedianSortedArrays(nums1, nums2)



