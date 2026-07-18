speed = int(input("Enter the speed for vehical:  "))
print(speed)
if speed <= 60:
    print("NO FINE")
elif 61 < speed < 80 :
    print("500 FINE")
elif 81 < speed < 100 :
    print("1000 FINE")
else :
    print("2000 FINE")
