def countJumps(c, index, count):
    if index == len(c)-1:
        return count
    elif index+2 < len(c) and c[index+2] == 0:
        return countJumps(c, index+2, count+1)

    elif index+1 < len(c) and c[index+1] == 0:
        return countJumps(c, index+1, count+1)


def jumpingOnClouds(c):
    count = 0
    return countJumps(c, 0, count)


if __name__ == '__main__':
    c = list(map(int, '0 0 0 0 1 0'.rstrip().split()))

    result = jumpingOnClouds(c)
