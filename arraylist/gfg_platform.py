def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    platform = {}
    count = 1
    platform[count] = dep[0]

    for i in range(1, len(arr)):
        alloted = True
        for j in platform:
            alloted = False
            if platform[j] < arr[i]:
                platform[j] = dep[i]
                alloted = True
                break
        if not alloted:
            count += 1
            platform[count] = dep[i]
    return count



if __name__ == '__main__':
    print(minimumPlatform(6,["0900",  "0940", "0950",  "1100", "1500", "1800"],["0910", "1200", "1120", "1130", "1900", "2000"]))


