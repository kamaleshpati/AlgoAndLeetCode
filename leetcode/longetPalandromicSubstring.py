class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        for i in range(0,len(s)):
            j = len(s)-1
            while j > i:
                if s[i] == s[j]:
                    print(s[i])
                    self.checkPalindrom(s,i,j)
                j-=1
    
    def checkPalindrom(self, s: str,start:int,end:int)->str:
        pass

print(Solution().longestPalindrome("babad"))