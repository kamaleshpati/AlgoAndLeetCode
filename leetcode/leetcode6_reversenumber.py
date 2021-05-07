class Solution:
    def reverse(self, x: int) -> int:
        if len(bin(x))>32:
            return 0
        rev = 0
        negetive = False if x >= 0 else True
        x = x * -1 if negetive else x
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
        return {True: rev * -1, False: rev}[negetive == True]




if __name__ == '__main__':
    print(Solution().reverse(1534236469))
