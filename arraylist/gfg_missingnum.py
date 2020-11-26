def MissingNumber(array, n):
    # code here
    res = 0
    for i in array:
        res += i
    print(sum(array))
    return (n * (n + 1) // 2) - res


if __name__ == '__main__':
    MissingNumber([1, 2, 3, 5], 5)