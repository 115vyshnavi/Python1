#Use a ternary expression to label a temperature as "hot", "mild", or "cold".
temp=int(input("Enter the temperature in Celsius: "))
label = "hot" if temp > 30 else "mild" if temp >= 15 else "cold"
print(f"The temperature is {label}.")