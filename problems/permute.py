class Permute:
    def getPermutation(self, n: int, k: int) -> str:
        s = ""
        self.k = k+1
        for i in range(n):
            s+=str(i+1)
        return self.permute(s,"")

    def permute(self,s, answer):
        if len(s) == 0:
            self.k -= 1
            if (self.k == 0):
                print(answer)
            return

        for i in range(len(s)):
            ch = s[i]
            left_substr = s[0:i]
            right_substr = s[i + 1:]
            rest = left_substr + right_substr

            self.permute(rest, answer + ch)




if __name__ == '__main__':
    print(Permute().getPermutation(3,4))