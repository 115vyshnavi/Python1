result = ""
for word in ["a", "b", "c"]:
    result += word + "-"
# preferred for many pieces
result = "-".join(["a", "b", "c"])
print(result)   
# 'a-b-c'