def outter(a,b ):
    def inner(a,b):
        return a+b
    add=inner(a,b)
    print(add)
    return add+5
result=outter(5,10)
print(result)

    #inner function accessing the value of a And b in it