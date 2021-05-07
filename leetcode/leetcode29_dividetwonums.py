class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = int(dividend / divisor)
        return answer if answer in range((-2)**31, (2**31 - 1)) else 2 ** 31 - 1


if __name__ == '__main__':
    print(Solution().divide(2147483647,2))
