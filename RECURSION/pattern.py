def pattern(number):
    if number == 1:
        print("1",end=",")
        return 1
    else:
        a=pattern(number-1) + 3
        print(a, end=",")
        return a
print(pattern(4))

