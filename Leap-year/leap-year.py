try:
    input_str = input("Enter two years separated by a comma: ")
    start_year, end_year = map(int, input_str.split(','))
    
    if start_year > end_year:
        start_year, end_year = end_year, start_year

    leap_years_count = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years_count += 1

    print(f"Number of leap years from {start_year} to {end_year}: {leap_years_count}")
except ValueError:
    print("Invalid input. Please enter two valid years separated by a comma.")
