income = float(input("Enter the annual income: "))

if income < 85528:
    tax = round((0.18*income)- 556.20)
    if tax < 0:
        print("The tax is 0.0 thalers")
    else:
        print("The tax is:", float(tax), "thalers")
else:
    tax = round(14839.20 + (0.32*(85528-income)))
    print("The tax is:", float(tax), "thalers")
# Write your code here.
#

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
