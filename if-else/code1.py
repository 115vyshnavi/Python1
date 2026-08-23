marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks < 50:
    print("Fail")
else:
    print("Pass")