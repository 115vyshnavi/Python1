#Create a list containing the squares of only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = [n*n for n in numbers if n%2==0]
print(result)