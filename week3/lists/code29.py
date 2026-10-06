n = int(input()) #4
dic = {i: i for i in range(1, n+1)}# range(1, 5)->1 2 3 4
#dic={1:1, 2:2, 3:3, 4:4}
print(dic)
total = sum(dic.values())#1+2+3+4=10
print(total)