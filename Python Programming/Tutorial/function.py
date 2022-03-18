
def introduction():
    print("Hello user!")

introduction()

def say_hi(name, age):
    print("Hi " + name + " who is currently " + str(age) + " years old.")

say_hi("Mike", 24)
say_hi("Levi", 30)

#return statements
def cube(x):
    return pow(x, 3)
    
result = cube(8)
print(result)