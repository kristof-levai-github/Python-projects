import math

try:
    leg1 = float(input("Enter the length of the first leg: "))
    if leg1 <= 0:
        print("Invalid input. Please enter a positive number.")
    else:
        leg2 = float(input("Enter the length of the second leg: "))
        if leg2 <= 0:
            print("Invalid input. Please enter a positive number.")
        else:
            hypotenuse = math.sqrt(leg1**2 + leg2**2)
            print(f"Hypotenuse: {hypotenuse}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
