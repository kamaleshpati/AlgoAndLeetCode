class Solution:
    def convert(self, s: str, numRows: int):
        if(numRows ==1):
            return s
        
        result = ""
        for i in range(0,numRows):
            start = i
            res = ""
            if(i == 0 or i == numRows-1):
                n = 2*(numRows-1)
                while start < len(s):
                    res += s[start]
                    start += n
            else:
                even = 2*(numRows-1-start)
                odd = 2*(start)
                turn = True

                while start < len(s):
                    res += s[start]
                    if(turn):
                        start += even
                        turn = False
                    else:
                        start += odd
                        turn = True
            
            
            
            # print(res)
            result += res
        return result
    




str = "PAYPALISHIRING"
sol = Solution()
sol.convert(str,3)