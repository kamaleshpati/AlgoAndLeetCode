

def permute(s,l,r):

    if l==r:
        print(s)
    else:
        for i in range(l,r+1):
            s = swap(s,l,i)
            permute(s,l+1,r)
            s = swap(s,l,i)


def swap(s,i,j):
    strlst = list(s)
    strlst[i], strlst[j] = strlst[j], strlst[i]
    return "".join(strlst)





s = "abc"
permute(s,0,len(s)-1)