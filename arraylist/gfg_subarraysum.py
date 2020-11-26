def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0

    i = 1
    while i <= n:
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            return start+1,i
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    return -1

if __name__ == '__main__':
    print(subArraySum([1, 2, 3, 7, 5],5,12))