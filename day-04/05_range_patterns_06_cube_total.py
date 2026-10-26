# Activity 4: Cubes and their total
import math
n = int(input("Enter a positive whole number: "))

if n < 1:
    print("Invalid input. Number must be at least 1.")
else:
    total = 0

    for number in range(1, n + 1):
        cube = math.pow(number,3)
        print(cube, end=", ")

        total = total + cube

print("\nTotal of cubes =", total)