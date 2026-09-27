n = [1, 2, 3, 4]
mx= n[0]
mn= n[0]
for num in n:
    if num>mx:
        mx = num
    if num<mn: 
        mn = num
print(f"Max: {mx}, Min:{mn}")
