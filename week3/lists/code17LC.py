#squares = [n * n for n in numbers] 
#List comprehension 
#For every n in numbers, put n*n into the new list.
numbers = [1, 2, 3, 4, 5, 6] 
even = [n for n in numbers if n % 2 == 0] #We want only even numbers. [expression for item in collection if condition]
#For each item, if the condition is true, put the expression into the list.

result = [n * 2 for n in numbers]  #----> [expression for item in collection]
print(result)

