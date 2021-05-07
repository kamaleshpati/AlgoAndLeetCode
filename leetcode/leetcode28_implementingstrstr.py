class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle)-1 and haystack[i+j] == needle[j]:
                        return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr("hello","ll"))