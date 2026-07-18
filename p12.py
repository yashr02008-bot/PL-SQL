n = int(input("enter the number:  "))
temp = n
sum = 0
t=None
while (n>0) :
    t = n % 10
    sum = sum+t*t*t
    n = n//10
if (temp == sum):
    print("number is armstrong number")
else:
    print("number is not armstrong number")
