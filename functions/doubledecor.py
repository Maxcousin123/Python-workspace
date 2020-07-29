def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner


def num():
    return 5

resultfun=decor(num)
print(resultfun())
#this is used to double result returned by function
def decor1(fun):
    def inner():
        result=fun()
        return result*2
    return inner
#another wayt to use decor function
@decor
def num1():
    return 5
print(num1())