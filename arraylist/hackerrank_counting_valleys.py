def getCount(pos, path, index, res):
    if index == len(path):
        return res
    elif path[index] == 'U':
        pos += 1
        if pos == 0:
            res += 1
        return getCount(pos, path, index + 1, res)
    else:
        pos -= 1
        return getCount(pos, path, index + 1, res)


def countingVelley(steps, path):
    pos = ({True: 1, False: -1})[path[0] is 'U']
    print(getCount(pos, path, 1, 0))


if __name__ == '__main__':
    countingVelley(8, "DDUUDDUDUUUD")
