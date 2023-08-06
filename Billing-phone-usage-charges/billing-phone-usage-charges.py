try:
    fc = int(input("Enter the number of foreign calls: "))
    onc = int(input("Enter the number of outside network calls: "))
    inc = int(input("Enter the number of inside network calls: "))

    fd = float(input("Enter the total duration of foreign calls (in minutes): "))
    ond = float(input("Enter the total duration of outside network calls (in minutes): "))
    ind = float(input("Enter the total duration of inside network calls (in minutes): "))

    ft = 100
    ont = 60
    int = 40

    fc_charges = fc * fd * ft
    onc_charges = onc * ond * ont
    inc_charges = inc * ind * int

    total_charges = fc_charges + onc_charges + inc_charges

    print(f"Total phone usage charges: {total_charges} HUF")
except ValueError:
    print("Invalid input. Please enter valid numbers for call counts and durations.")
