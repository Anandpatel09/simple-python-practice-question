def myFunc(*args):
       print(args)       
myFunc(1,2,3,4,5,6,7,)
myFunc(9,8,7,6,5,4,3,2,1)



#same thing using for loop
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)