l = [1,2,3,5,5,3,1]
dic = {} 

for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic) # {1:2, 2:1, 3:2, 5:2}
print(dic.get(4))
print(dic.get(3))