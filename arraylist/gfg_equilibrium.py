def equilibriumPoint(A, N):

    if N==1:
        return A[0]
    res = sum(A) - A[0]
    res2 =  A[0]
    for i in range(1,len(A)):
        res -= A[i]
        if res2 == res:
            return i+1
        res2+=A[i]
    return -1

if __name__ == '__main__':
    print(equilibriumPoint([20, 17, 42, 25, 32, 32, 30, 32, 37, 9, 2, 33, 31, 17, 14, 40, 9, 12, 36, 21, 8, 33, 6, 6, 10, 37, 12, 26, 21, 3],30))