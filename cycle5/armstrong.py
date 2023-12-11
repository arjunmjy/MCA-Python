def is_armstrong_number(number):
    # Convert the number to a string to get individual digits
    num_str = str(number)
    num_digits = len(num_str)
    # Calculate the sum of the nth power of each digit
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    return armstrong_sum == number

