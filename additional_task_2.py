def digit_root(num):
    while len(num) > 1:
        num = str(sum([int(i) for i in num]))
    return num
print(digit_root(input()))