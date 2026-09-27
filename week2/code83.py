n = int(input("Enter a number: "))

total = 0
count = 0

for digit in str(n):
    total += int(digit)
    count += 1

average = total / count

print(average)