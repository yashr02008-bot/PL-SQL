n=int(input("enter the no:  "))
sum=0
flag=1
for i in range(1,n+1,2):
    sum=sum+(i*flag)
    flag=flag*-1
print(sum)