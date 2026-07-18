n = int(input("enter the number:  "))
sum = 0
temp=n
while (n>0):
    rem=n%10
    sum=sum*10+rem
    n=n//10

if(temp==sum):
    print("number is paldrom")
else:
    print("number is not palidrom")