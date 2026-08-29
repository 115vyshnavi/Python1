cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))
profit = sp - cp
status = "Profit" if profit > 0 else "Loss" if profit < 0 else "No Profit or Loss"
print(f"{status}: {profit}")
