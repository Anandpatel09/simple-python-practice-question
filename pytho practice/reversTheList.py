list1 = [10, 20, 30, 40, 50]
length=len(list1)
for i in range(length):
    print(list1[length-i-1])
    # above is my logic 
    
# with the help of reversed function
print("\n")
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)
        