s = input("Enter a text: ")
for char in s:
    if s.count(char)==1:
        print("First non - repeating charcater:", char)
        break
