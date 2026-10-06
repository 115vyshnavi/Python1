#Write a Python program to calculate the total of all numerical values stored in a dictionary
dic = {
    "yshu": 90,
    "lucky": 85,
    "uma": 75
}
total = 0
for value in dic.values():
    total += value
print(total)