python = int(input("Enter Python Marks: "))
sql = int(input("Enter SQL Marks: "))
dsa = int(input("Enter DSA Marks: "))
def calculate_total(python, sql, dsa):
    total_marks = python + sql + dsa
    average = total_marks / 3
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return total_marks, average, grade
total, average, grade = calculate_total(python, sql, dsa)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)