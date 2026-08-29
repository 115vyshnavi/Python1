age = input("Enter your age: ")
score = int(input("Score: "))
eligible = age >= 18 and score >= 70
print("Eligible" if eligible else "Not Eligible")
