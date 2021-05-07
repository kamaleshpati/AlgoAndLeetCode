class Solution:
    def isValid(self, s: str) -> bool:
        listAsStack = []
        for ch in s:
            if ch in ["(", "{", "["]:
                listAsStack.append(ch)
            else:
                if len(listAsStack) is 0:
                    return False
                top = listAsStack.pop()
                if top == '(':
                    if ch != ")":
                        return False
                if top == '{':
                    if ch != "}":
                        return False
                if top == '[':
                    if ch != "]":
                        return False

        if len(listAsStack) is not 0:
            return False
        return True
