age = int(input("Enter the age: "))

has_permit = False

result = "valid" if (18 <= age <= 60) or has_permit else "invalid"

print(result)