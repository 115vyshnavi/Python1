def calculate_salary(basic_salary, bonus=5000, tax_rate=10):
    gross_salary = basic_salary + bonus
    tax = gross_salary * tax_rate / 100
    net_salary = gross_salary - tax
    return gross_salary, tax, net_salary
gross, tax, net = calculate_salary(30000)
print("Gross Salary:", gross)
print("Tax:", tax)
print("Net Salary:", net)