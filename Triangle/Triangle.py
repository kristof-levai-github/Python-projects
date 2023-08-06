import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def main():
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        
        if a <= 0 or b <= 0 or c <= 0:
            print("Invalid input. Length of sides must be positive.")
            return

        area = calculate_area(a, b, c)
        perimeter = calculate_perimeter(a, b, c)
        
        print(f"Area: {area:.2f}")
        print(f"Perimeter: {perimeter:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
