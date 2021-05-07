from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) is 0:
            return ""

        res = ""
        smallest = strs[0]
        for i in strs:
            if len(i) < len(smallest):
                smallest = i

        for i in range(len(smallest)):
            for j in strs:
                if j[i] != smallest[i]:
                    return res
            res += smallest[i]
        return res


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))



