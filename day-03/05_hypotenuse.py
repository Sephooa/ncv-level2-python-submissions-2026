# Hypotenuse of a right-angled triangle
import math

side_a = float(input("Enter side A in metres: "))
side_b = float(input("Enter side B in metres: "))

if side_a <= 0:
    print("Side A must be greater than zero.")
else:
    if side_b <= 0:
        print("Side B must be greater than zero.")
    else:
        hypotenuse = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
        print(f"Hypotenuse: {hypotenuse:.2f} m")
