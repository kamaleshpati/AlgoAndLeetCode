class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        start = 0
        longest = 1
        while start+longest+1<len(s):
            pos = self.findOcurance(s[start:start+longest])
            if pos == -1:
                longest += 1
            else:
                start = start+pos+1
        return longest
    
    def findOcurance(self, s: str) -> int:
        for x in range(1,len(s)):
            if s.find(s[x])!=x:
                return s.find(s[x])
        return -1
            
        


print(Solution().lengthOfLongestSubstring("abcb"))



