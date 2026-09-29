#Sort the list in descending order without changing the original list.
#Print both the sorted result and original list.
marks = [78, 95, 62, 88, 70]
m = marks.copy()
m.sort(reverse=True)
print(m)
print(marks)