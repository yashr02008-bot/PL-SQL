n=int(input("enter the number:  "))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
    if(count>2):
        break
print(count)
if(count==2):
    print("number",n,"is prime number:")
else:
    print("number",n," is not prime number");