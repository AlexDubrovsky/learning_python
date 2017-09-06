def rus_peasant(a, b):
    res = 0
    while a > 0:
        if a % 2 != 0:
            res += b
        a >>= 1
        b <<= 1
    return res

num1 = 13
num2 = 238
print rus_peasant(num1, num2)
print '{} * {} = {}'.format(num1, num2, num1*num2)
