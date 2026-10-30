balance = int(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = int(input("Enter amount: "))

    if choice == 1:
        balance = balance + amount
        print("Deposit successful")

    elif choice == 2:
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    else:
        print("Invalid choice")

print("Final Balance =", balance)13