a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))
d = int(input("enter value of d:"))
print(a,b,c,d);
if a>b and a>c and a>d:
    print(a,"max");
elif b>a and b>c and b>d:
    print(b,"max");
elif c>a and c>b and c>d:
    print(c,"max");
else :
    print(d,"max");      