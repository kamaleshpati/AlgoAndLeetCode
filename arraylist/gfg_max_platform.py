
def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    platform  = 1
    alloted = True
    for i in range(1,n):
        for j in range(0,i):
            if dep[j] > arr[i]:
                alloted = False
            else:
                alloted = True

        if alloted == False:
            platform += 1
            alloted = True




    return platform





if __name__ == '__main__':
    arr = ["0900",  "0940", "0950",  "1100", "1500","1800"]
    dep = ["0910", "1200", "1120", "1130", "1900", "2000"]
    print(minimumPlatform(6,arr,dep))