num=int(input("enter the number whose factorial is to be found ?"))
factorial=1
for i in range (num,0,-1):
    factorial=factorial*i
print(factorial)        