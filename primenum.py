cnt=0
n=int(input("enter numebr:::"))
for i in range(1,n+1):
    if(n%i==0):
        cnt+=1
    if(cnt>2):
        break;
print(cnt)
if(cnt==2):
    print("number is prime")
else:
    print("number in not prime")