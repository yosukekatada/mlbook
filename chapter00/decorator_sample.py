def mydecorator(f):
    def _mydecorator(*args, **kwargs):
        print('before')
        result = f(*args, **kwargs)
        print('after')
        return result
    return _mydecorator

@mydecorator
def myfunc(x):
    return x ** 2

print(myfunc(3))  # =>
                  # before
                  # after
                  # 9

print(mydecorator(myfunc)(3))  # => same as above
