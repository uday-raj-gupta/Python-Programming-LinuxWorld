print("Attendence Calculator")
pastClasses = int(input("Total no of classes: "))
attendClasses = int(input("Total attended classes: "))

currentPercentage = (attendClasses / pastClasses) * 100
print(f"Your current attendance = {currentPercentage:.2f}%")

print("What is your target Percentage?")
targetpercent = float(input())

upclasses = int(input("No of upcoming classes: "))

totalclasses = pastClasses + upclasses
requireclass = (targetpercent / 100) * totalclasses
neededclass = requireclass - attendClasses

allattend = attendClasses + upclasses
allattendpercent = (allattend / totalclasses) * 100

# Main Logic
if neededclass > upclasses:
    print("Target Not Achievable")
    print(f"You need to attend {neededclass:.2f} classes but there are only {upclasses} upcoming classes.")

    print("Do you want to know what your percentage will be if you attend ALL upcoming classes?")
    choice = int(input("Press 1 for YES, 2 for NO: "))

    if choice == 1:
        print(f"You will have {allattendpercent:.2f}% if you attend all upcoming classes.")
    else:
        print("Okay, thank you!")

elif neededclass == upclasses:
    print("Target Achievable!")
    print(f"You need to attend {neededclass:.2f} classes. You must attend ALL upcoming classes!")

else:  # neededclass < upclasses
    print("Target Achievable!")
    print(f"You need to attend {neededclass:.2f} classes out of {upclasses} upcoming classes.")
