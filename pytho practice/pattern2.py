#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1
for i in  range(5,0,-1) :
    for j in range(i,0,-1):
        print(j,end="")
    print("\n")    
 
print("drawing another pattern")  
 
#Draw the pattern
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2 
#1
for i in  range(5,0,-1) :
    for j in range(i,0,-1):
        print(i,end="")
    print("\n")    