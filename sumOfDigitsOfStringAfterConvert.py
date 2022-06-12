def getLucky(s, k):
    import string
    letterToNumberMap = dict(zip(string.ascii_lowercase, range(1,27)))
    theString = ''
    for s_ in s:
        theString += str(letterToNumberMap[s_])
    ans = 0
    for i in range(k):
        ans = sum([int(theString[j]) for j in range(len(theString))])
        theString = str(ans)
    return ans

print(getLucky("leetcode", 2))