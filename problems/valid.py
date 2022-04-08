class Valid:
    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False
        elif len(s) == 1:
            if s.isdigit() or s.isdecimal():
                return True
        for i in range(len(s)):
            pass

