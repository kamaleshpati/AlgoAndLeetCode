from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        open_bracket_so_far = 0
        close_bracket_so_far = 0
        self.generateParenthesisPattern(combinations, "", open_bracket_so_far, close_bracket_so_far, n)
        return combinations

    def generateParenthesisPattern(self, combinations, current_str, open_bracket_so_far, close_bracket_so_far, n):
        if len(current_str) == n * 2:
            combinations.append(current_str)
            return
        if open_bracket_so_far < n:
            self.generateParenthesisPattern(combinations, current_str + "(", open_bracket_so_far + 1,
                                            close_bracket_so_far, n)
        if close_bracket_so_far < open_bracket_so_far:
            self.generateParenthesisPattern(combinations, current_str + ")", open_bracket_so_far,
                                            close_bracket_so_far+1, n)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))







