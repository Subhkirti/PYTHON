def pattern(number):
    if number == 1:
        return 10
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    else:
        return pattern(number - 1) * 10
print(pattern(4))