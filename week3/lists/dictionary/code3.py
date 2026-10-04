#Dictionary CRUD Operations

#Create a dictionary
student = {
    "name": "Vyshnavi",
    "age": 20,
    "marks": 95
}
print(student)

#Add a new key-value pair
student["branch"] = "CSE"
print(student)

#Access a value
print(student["name"])

#Safe access using get()
print(student.get("phone", "Not Available"))

#Read all keys
print(student.keys())

#Read all values
print(student.values())

#Read key + value
print(student.items())