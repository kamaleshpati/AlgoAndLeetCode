class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.isPalndromicString(str(x))

    def isPalndromicString(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(12111))