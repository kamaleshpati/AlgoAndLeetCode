from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        permute_strings = allPermutation(words)
        considered_length = len(permute_strings[0])
        for i in range(len(s)-considered_length+1):
            for j in permute_strings:
                if s[i:i+considered_length] == j:
                    res.append(i)
                    break
        return res


def findPermutePattern(li,res,string):
    if len(li) == 1:
        string += li[0]
        res.append(string)
    else:
        for i in range(len(li)):
            li[0],li[i] = li[i],li[0]
            findPermutePattern(li[1:],res,string+li[0])
            li[0], li[i] = li[i], li[0]




def allPermutation(li):
    res = []
    findPermutePattern(li,res,"")
    return res


if __name__ == '__main__':
    print(Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))