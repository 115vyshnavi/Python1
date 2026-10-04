a= {"x": 1, "y": 2}
b = {"y": 9, "z": 3}
merged = {**a, **b}    
merged = a | b         
a |= b                 
# {'x':1, 'y':9, 'z':3}  -> b wins on clash
# Python 3.9+ merge operator, same result
# in-place merge/update
# Nested dict -- e.g. students -> subject -> marks
records = {
"Asha": {"math": 92, "cs": 88},
"Ravi": {"math": 75, "cs": 95},
}
records["Asha"]["cs"]              
records["Ravi"]["math"] = 80  