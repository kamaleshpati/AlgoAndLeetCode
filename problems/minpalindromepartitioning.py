class MinPartition:
    def isPalindrome(self, x):
        return x == x[::-1]

    def minPartition(self, s, i, j):
        if i >= j or self.isPalindrome(s[i:j + 1]):
            return 0
        ans = float('inf')
        for k in range(i, j):
            count = (
                    1 + self.minPartition(s, i, k)
                    + self.minPartition(s, k + 1, j)
            )
            ans = min(ans, count)
        return ans

    def minCut(self, s: str) -> int:
        return self.minPartition(s,0, len(s)-1)


