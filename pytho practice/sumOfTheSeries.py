num=5
startSeries=2
SumOfSeries=0
total=0
for i in range (1,num+1):
    print(startSeries,end="+")
    SumOfSeries =startSeries
    total+=SumOfSeries
    startSeries=SumOfSeries*10+2
print("sum of above series is =",total )    