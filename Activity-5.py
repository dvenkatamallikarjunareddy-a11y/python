subjects = ["Python", "Maths", "English"]

for subject in subjects:
    first = int(input("Enter first exam marks: "))
    second = int(input("Enter second exam marks: "))

    difference = second - first

    print("Subject:", subject)

    if difference > 0:
        print("Improved by", difference, "marks")
    elif difference < 0:
        print("Declined by", -difference, "marks")
    else:
        print("No change")

    if second < 35:
        print("Weak subject")
    else:
        print("Good performance")