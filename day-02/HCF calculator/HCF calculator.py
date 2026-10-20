# Input
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Selection: Validate inputs and select the smaller number
if x <= 0 or y <= 0:
    print("Please enter positive whole numbers.")

else:
    # Selection: Assign the smaller number to factor
    if x > y:
        factor = y
    else:
        factor = x

    # Iteration: Find the HCF
    while x % factor != 0 or y % factor != 0:
        factor = factor - 1

    # Output
    print("The HCF is:", factor)