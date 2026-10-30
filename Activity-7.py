
password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch >= "A" and ch <= "Z":
        upper = upper + 1
    elif ch >= "a" and ch <= "z":
        lower = lower + 1
    elif ch >= "0" and ch <= "9":
        digit = digit + 1
    else:
        special = special + 1

if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Strong Password")
else:
    print("Weak Password")