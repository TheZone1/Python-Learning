
def power(base_num, pow_num):
    return float(pow(base_num, pow_num))

print(power(3, 5))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(3, 3))
