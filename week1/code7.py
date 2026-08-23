def calculate_average(*marks):

    total = sum(marks)
    average = total / len(marks)

    return average


def find_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def display_result(name, *marks):

    average = calculate_average(*marks)
    grade = find_grade(average)

    print("Name:", name)
    print("Marks:", *marks)
    print("Average:", average)
    print("Grade:", grade)


display_result("vyshnavi", 85, 78, 92, 88)
