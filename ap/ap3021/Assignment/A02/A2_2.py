# The function to convert float type into integer type.

print("The function we convert float type into integer type in python is: int()\n")

""" The example of the python code to convert float type to int type. """

print("====== The First Experiment ======")
# First we announce the float type number.
numberOne = 10.0000000001

print(f"The numberOne: {numberOne};\tType: {type(numberOne).__name__}.")

# After using the function, it will ignore the value after point.
numberOne = int(numberOne)
print(f"The converted numberOne: {numberOne};\tConverted type: {type(numberOne).__name__}.")

print("\n====== The Second Experiment ======")

# The next we can do another experiment, we announce the second number.
numberTwo = 10.9999999999
print(f"The numberTwo: {numberTwo};\tType: {type(numberTwo).__name__}.")

# After using the function, it still ignore the value after point.
# No matter the value after the point. The result is the same.
numberTwo = int(numberTwo)
print(f"The converted numberTwo: {numberTwo};\tConverted type: {type(numberTwo).__name__}.\n")

print("====== The conclusion ======")
print("Above all, we know that if we use function int() in python, no matter how value after the point, it will be losed.")


"""

The function we convert float type into integer type in python is: int()

====== The First Experiment ======
The numberOne: 10.0000000001;   Type: float.
The converted numberOne: 10;    Converted type: int.

====== The Second Experiment ======
The numberTwo: 10.9999999999;   Type: float.
The converted numberTwo: 10;    Converted type: int.

====== The conclusion ======
Above all, we know that if we use function int() in python, no matter how value after the point, it will be losed.

"""
