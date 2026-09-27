n = [1,2,2,3,4]
dupli = list(set([a for a in n if n.count(a)>1]))
print(dupli)