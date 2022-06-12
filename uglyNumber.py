def isUgly(n):
    if n==0:
        return False
    if n==1:
        return True
    factors = []
    if n%2==0:
        factors.append(2)
    if n%3==0:
        factors.append(3)
    if n%5==0:
        factors.append(5)
    if len(factors)==0:
        return False
    while n!=1:
        flag = 0
        for factor in factors:
            if n%factor==0:
                n = n/factor
                flag = 1
        if flag==0:
            return False

    return True
        
print(isUgly(100))

