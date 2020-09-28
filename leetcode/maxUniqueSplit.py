class Solution:
    def maxUniqueSplit(self,s)->int:
        dict = {}
        print(self.recusiveAdd(dict,s,0,1))
        return len(self.recusiveAdd(dict,s,0,1))

    def recusiveAdd(self,dict:dict,s:str,start:int,length:int)->dict:
        if start+length >= len(s):
            if dict.get(s[start:len(s)+1]) is None:
                dict[s[start:start+length]] = length
            return dict
        else:

            if dict.get(s[start:start+length]) is None:
                dict[s[start:start+length]] = length
                return self.recusiveAdd(dict,s,start+length,1)
            else:
                return self.recusiveAdd(dict,s,start+length,length+1)


s = "ababccc"
print(Solution().maxUniqueSplit(s))
