n = int(input("enter the number:  "))
temp = n
sum = 0
while (n<0):
    temp = n%10
    sum = sum*10+temp
    n = n//10

print("sum of digit is",n)