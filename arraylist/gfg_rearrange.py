def rearrange(arr, n):
    res = []
    for i in range(0,len(arr)//2):
        res.append(arr[n-1-i])
        res.append(arr[i])

    if n %2 != 0:
        res.append(arr[len(arr)//2])
    for i in range(len(arr)):
        arr[i] = res[i]



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    rearrange(arr,7)
    print(arr)