"""In this question i am using the decorator"""
def validate_range(min_value, max_value):
    """
    This decorator validates if the argument passed to the function is within the specified range.
    """
    def decorator(func):
        def wrapper(arg):
            if min_value <= arg <= max_value:
                return func(arg)
            raise ValueError(f"Arg {arg} isn't within the given range [{min_value}, {max_value}]")
        return wrapper
    return decorator

@validate_range(1, 10)
def generate_sequence_of_squares(arg):
    """
    This function generates a sequence of squares of all even numbers in the range of 1 to 10.
    """
    return [x ** 2 for x in range(1, arg+1) if x % 2 == 0]

result = generate_sequence_of_squares(10)
print(result)
