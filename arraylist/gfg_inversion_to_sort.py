def countInversionFromBubbleSort(arr):
    count = 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1

    return count


if __name__ == '__main__':
    arr = [2, 4, 1, 3, 5]

    print(countInversionFromBubbleSort(arr))
