venue = int(input("Enter venue cost: "))
equipment = int(input("Enter equipment cost: "))
catering = int(input("Enter catering cost: "))
transport = int(input("Enter transport cost: "))
certificates = int(input("Enter certificate cost: "))

participants = int(input("Enter number of participants: "))
fee = int(input("Enter registration fee: "))

total = venue + equipment + catering + transport + certificates
income = participants * fee

print("Total Expenses =", total)
print("Total Income =", income)

if income >= total:
    print("Event is financially successful")
else:
    print("Additional funds required =", total - income)