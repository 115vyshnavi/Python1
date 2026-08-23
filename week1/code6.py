def find_largest(*numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
result = find_largest(10, 25, 7, 45, 18)
print("Largest Number:", result)
