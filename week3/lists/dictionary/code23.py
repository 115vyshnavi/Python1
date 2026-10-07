stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
v = float("inf")
k = None
for key, value in stock.items(): 
    if value < v: 
        v = value
        k = key 
print("Lowest stock item:", k)