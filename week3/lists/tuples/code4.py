lst=[1,2,3]
subsets=[[]]
for num in lst:
    new_subsets=[]
    for s in subsets:
        new_subsets.append(s+[num])
    subsets+=new_subsets
print(subsets)