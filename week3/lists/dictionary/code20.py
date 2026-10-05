student = {
    "name": "Asha",
    "marks": 95,
    "branch": "CSE"
}

for i, (key, value) in enumerate(student.items(), start=1):
    print(i, key, value)