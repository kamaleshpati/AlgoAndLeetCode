
def repeatedString(s, n):

    if len(s) == 1:
        if s[0] == 'a':
            return n
        else:
            return 0

    else:
        count = 0
        aPos = []
        minimum = n//len(s)
        calc = n % len(s)
        for i in range(len(s)):
            if s[i] == 'a':
                aPos.append(i)
        count += len(aPos)*minimum
        for i in aPos:
            if i < calc:
                count += 1
            else:
                break
        return count


if __name__ == '__main__':
    result = repeatedString('aBa', 10)
    print(result)