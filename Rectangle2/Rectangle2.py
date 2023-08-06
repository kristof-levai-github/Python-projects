try:
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    surface_area = 2 * (a * b + a * c + b * c)
    volume = a * b * c

    print(f"Surface Area: {surface_area}")
    print(f"Volume: {volume}")
except ValueError:
    print("Invalid input. Please enter valid numbers for the lengths of sides.")
