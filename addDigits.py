def addDigits(num):
    if len(str(num))==1:
        return num
    while True:
        l = [int(d) for d in str(num)]
        num = sum(l)
        if len(str(num))==1:
            return num

print(addDigits(38))