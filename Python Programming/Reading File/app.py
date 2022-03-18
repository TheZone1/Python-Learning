
employee_file = open("Reading File/employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)
employee_file.close()

