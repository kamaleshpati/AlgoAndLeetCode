from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []
        if digits:
            self.backtrack("", digits, phone,output)
        return output

    def backtrack(self, combination, next_digits, phone, output):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                self.backtrack(combination + letter, next_digits[1:],phone, output)


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))



