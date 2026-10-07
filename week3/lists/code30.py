stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_value = min(stock.values())
for key in stock.keys():
    if stock[key] == min_value:
        print("Lowest stock item:", key)