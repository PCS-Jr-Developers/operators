# Get user inputs for the first number and the second number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Equal (==)
result_equal = num1 == num2  # Is the first number the same as the second number?
print(str(num1) + " == " + str(num2) + ": " + str(result_equal) + "\n")

# Not Equal (!=)
result_not_equal = num1 != num2  # Is the first number different from the second number?
print(str(num1) + " != " + str(num2) + ": " + str(result_not_equal) + "\n")

# Greater Than (>)
result_greater_than = num1 > num2  # Is the first number bigger than the second number?
print(str(num1) + " > " + str(num2) + ": " + str(result_greater_than) + "\n")

# Less Than (<)
result_less_than = num1 < num2  # Is the first number smaller than the second number?
print(str(num1) + " < " + str(num2) + ": " + str(result_less_than) + "\n")

# Greater Than or Equal To (>=)
result_greater_equal = num1 >= num2  # Is the first number bigger than or equal to the second number?
print(str(num1) + " >= " + str(num2) + ": " + str(result_greater_equal) + "\n")

# Less Than or Equal To (<=)
result_less_equal = num1 <= num2  # Is the first number smaller than or equal to the second number?
print(str(num1) + " <= " + str(num2) + ": " + str(result_less_equal) + "\n")
