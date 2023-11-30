def addIntegers(*args):
    """
    This function takes variable-length integer arguments and returns their sum.

    Parameters:
    *args : int
        Variable-length arguments of integers to be added.

    Returns:
    int
        Sum of the provided integers.
    """
    if not args:
        return 0
    else:
        return sum(args)
input_numbers=input("Enter integers seperated by spaces : ").split()
input_numbers=[int(num) for num in input_numbers]
result=addIntegers(*input_numbers)
print("The sum of the integers is : ",result)

