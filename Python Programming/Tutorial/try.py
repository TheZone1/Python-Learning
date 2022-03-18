#can be used to protect the program
try: 
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid Input")