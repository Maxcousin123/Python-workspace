def decorfun(fun):
    def inner(n):
        result=fun(n)
        result=result+'how are u'
        return result
    return inner

@decorfun
def hello(name):    
    return'hello'+name

print(hello('john'))