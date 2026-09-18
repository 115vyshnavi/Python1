raw = input("Enter your age: ")
try:
    age = int(raw)
    print(f"Double your age is {age * 2}")
except ValueError:
    print(f"'{raw}' is not a valid whole number.")