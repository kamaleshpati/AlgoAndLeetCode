def leaders(A,N):
    if N == 1:
        return A[0]

    ans = [A[len(A)-1]]
    max = ans[0]
    for i in range(len(A)-2,-1,-1):
        if A[i]>=max:
            max = A[i]
            ans.append(max)

    return ans[::-1]

if __name__ == '__main__':
    print(leaders([1, 2, 3, 4, 0],5))