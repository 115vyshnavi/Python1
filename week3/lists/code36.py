lst = [1, 2, 3]
print([])  # Empty subset
for i in range(len(lst)):
    print([lst[i]])  # Single element subsets
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        print([lst[i], lst[j]])  # Two element subsets
print(lst)  # Complete list