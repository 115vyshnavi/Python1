#Count the frequency of every character.
s = input("enter a String: ")
f={}
for char in s:
    f[char] = s.count(char)
print("Frequencies:", f)