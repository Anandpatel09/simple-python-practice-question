sum=0
def recursive(a):
    if a!=0:       
       return a + recursive(a-1)
    else:
       return 0
result=recursive(10)
print(result)

a#bove is my logic

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)
