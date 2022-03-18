is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
elif is_tall and not(is_male):
    print("You are tall but not a male.")
elif is_male and not(is_tall):
    print("You are Levi. ;)")
else:
    print("You are neither male or tall.")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 54, 56))