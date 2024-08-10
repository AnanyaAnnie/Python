# WAP  to create a decorator which waits 3 seconds to return the results.
def delay(func):
    def inner(*args, **kwargs):
        sleep(3)
        res = func(*args, **kwargs)
        return res
    return inner


@delay
def add(a, b, c, d):
    return a + b + c + d

@delay
def sub(a,b, c):
    return a - b - c

@delay
def mul(a, b, c):
