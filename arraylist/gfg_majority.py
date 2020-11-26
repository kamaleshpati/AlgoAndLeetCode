def majorityElement(A,N):
    eleDict = {}
    for i in A:
        if i in eleDict:
            eleDict[i] += 1
        else:
            eleDict[i] = 1
    major = 0
    majorEle = 0
    for i in eleDict:
        if eleDict[i] > major:
            major = eleDict[i]
            majorEle = i
    return ({True:-1, False:majorEle})[ major<=N/2 or major==1]

if __name__ == '__main__':
    print(majorityElement([6, 1, 15, 19, 9, 13, 12, 6, 7, 2, 10, 4, 1, 14 ,11 ,

14 ,14 ,13],18))