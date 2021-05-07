class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            visited = [False] * 256
            for j in range(i, len(s)):
                if visited[ord(s[j])]:
                    break
                else:
                    res = max(res, j - i + 1)
                    visited[ord(s[j])] = True
            visited[ord(s[i])] = False
        return res


if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))