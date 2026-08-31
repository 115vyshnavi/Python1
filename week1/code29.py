hits = 0
def visit():
global hits
hits += 1
visit(); visit()
print(hits)