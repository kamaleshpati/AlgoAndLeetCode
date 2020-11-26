class Solution:
    def reorderSpaces(self, text: str) -> str:
        if len(text) <= 1:
            return text
        arr = []
        spaces = 0
        ele = ""
        for i in text:
            if i is " ":
                spaces += 1
                if ele is not "":
                    arr.append(ele)
                    ele = ""
            else:
                ele += i
        if ele is not "":
            arr.append(ele)
        if len(arr) is 1:
            return arr[0]+spaces*" "
        mid = spaces // (len(arr) - 1)
        extra = spaces % (len(arr) - 1)
        ans = ""
        for i in range(0, len(arr)):
            if i < len(arr) - 1:
                ans += arr[i] + (" ") * mid
            else:
                ans += arr[i]
        if extra > 0:
            ans += (" ") * extra
        return ans

print(Solution().reorderSpaces("  this   is  a sentence "))