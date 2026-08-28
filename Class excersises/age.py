citizin = input("Are you a citizen? (yes/no): ")
if citizin.lower() == "yes":
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are under rage.")
else:
    print("You are not eligible to vote.")
score = int(input("Enter your point of exam: "))
if score >= 90:
    print("You grade is A1.")
elif score >= 80:
    print("You grade is A2.")
elif score >= 70:
    print("You grade is B1.")
elif score >= 60:
    print("You grade is B2.")
elif score >= 50:
    print("You grade is C.")
else:
    print("You Failed.")
