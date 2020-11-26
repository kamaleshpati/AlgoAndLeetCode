def trappingWater(arr, n):
    res = 0;
    for i in range(1, n - 1):
        left = arr[i];
        for j in range(i):
            left = max(left, arr[j]);
        right = arr[i];

        for j in range(i + 1, n):
            right = max(right, arr[j]);

        res = res + (min(left, right) - arr[i]);

    return res

def findWater(arr,n):
    left = [0] * n
    right = [0] * n
    water = 0
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


def findWaterRes(arr, n):
    result = 0
    left_max = 0
    right_max = 0

    lo = 0
    hi = n - 1

    while (lo <= hi):
        if (arr[lo] < arr[hi]):
            if (arr[lo] > left_max):
                left_max = arr[lo]
            else:
                result += left_max - arr[lo]
            lo += 1

        else:

            if (arr[hi] > right_max):
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result


if __name__ == '__main__':
    print(findWater([1, 1, 5, 2, 7, 6, 1, 4, 2, 3], 10))
