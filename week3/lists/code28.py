t = "hello world"
dic = {}
for char in t:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
print(dic)