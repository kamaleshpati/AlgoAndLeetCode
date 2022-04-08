class TextJust:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lens = [len(words[i]) for i in range(len(words))]
        res = []
        s = ""
        for i in range(len(words)):
            if(len(s)>0):
                s += " "
            if len(s)+lens[i]<maxWidth:
                s += words[i]
            else:
                if len(s)+lens[i]==maxWidth:
                    res.append(s)
                else:
                    gap = maxWidth-len(s)
                    word = s.split(" ")
                    if len(word)>1:
                        l = gap // (len(word)-1)
                        r = gap % (len(word)-1)
                        lgap, rgap = "", ""
                        for i in range(l):
                            lgap += " "

                        for i in range(r):
                            rgap += " "
                        s.replace(" ",lgap)
                        s+=rgap
                        res.append(s)
                        s = words[i]
                    else:
                        rgap = ""
                        for i in range(gap):
                            rgap += " "
                        s += rgap
                        res.append(s)


        return res

