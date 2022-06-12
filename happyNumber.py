def isHappy(n):
    visitedLists = []
    while True:
        l = [int(d) for d in str(n)]
        if l in visitedLists:
            return False
        visitedLists.append(l)
        s = 0
        for num in l:
            s += int(num)**2
        if s==1:
            return True
        if s<1:
            return False
        n = s
    
print(isHappy(2))