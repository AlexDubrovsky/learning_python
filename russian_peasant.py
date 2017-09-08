import time


CACHE = {}


def rus_peasant(a, b):
    key = (a, b)
    if key in CACHE:
        res = CACHE[key]
    else:
        res = 0
        while a > 0:
            if a % 2 != 0:
                res += b
            a >>= 1
            b <<= 1
    return res


def test_russian(a, b):
    assert rus_peasant(a, b) == a * b
    start_time = time.time()
    print start_time
    print rus_peasant(a, b)
    print time.time()
    print 'The algorithm took %f seconds' % (time.time() - start_time)


test_russian(1234374578578678962341234, 1234122454588956562341234341234)
# test_russian(13, 238)

# num1 = 13
# num2 = 238
# print rus_peasant(num1, num2)
# print '{} * {} = {}'.format(num1, num2, num1*num2)
