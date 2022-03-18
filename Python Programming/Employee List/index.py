

# r = read
# w = write
# a = add
# r+ = read and write

employee_file = open("Employee List/employee.txt", "r")
print(employee_file.readable())
employee_file.close()