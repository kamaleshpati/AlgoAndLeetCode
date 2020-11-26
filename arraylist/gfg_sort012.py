def defSort(arr):
    eleDict = [0, 0, 0]

    for i in arr:
        eleDict[i] += 1
    arr.clear()
    for i in range(len(eleDict)):
        for k in range(eleDict[i]):
            arr.append(i)


if __name__ == '__main__':
    arr = [0,1,2, 0]
    defSort(arr)
    print(arr)