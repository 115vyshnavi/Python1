price = float(input("Enter price: "))
discount = float(input("Enter Discount amount %: "))
bill = price - (price * discount / 100)
print(f"Total Bill amount: {bill}")
