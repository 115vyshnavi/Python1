s = input("Enter a Text: ")
s = s.lower()
vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
total = 0
for cons in s:
    if cons >= 'a' and cons <='z':
        total +=1
consonants = total - vowels 
print(f"Vowels: {vowels} \t Consonants: {consonants}")