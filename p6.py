income = int(input("Enter your income:  "))
print(income)
if income >= 100000 :
    print("Premium Loan")
elif income >= 50000 :
    print("Standard Loan")
elif income >= 25000 :
    print("Basic Loan")
else :
    print("Not Eligible")
    
