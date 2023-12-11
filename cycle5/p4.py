from armstrong import is_armstrong_number

def generate_armstrong_numbers(lower_limit, upper_limit):
    armstrong_numbers = []

    for number in range(lower_limit, upper_limit + 1):
        if is_armstrong_number(number):
            armstrong_numbers.append(number)

    return armstrong_numbers

lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))
result = generate_armstrong_numbers(lower_limit, upper_limit)

print(f"Armstrong numbers between {lower_limit} and {upper_limit} :")
print(result)

