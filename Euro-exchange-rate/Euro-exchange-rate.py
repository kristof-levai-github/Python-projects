def read_positive_real_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    exchange_rates = []
    count_below_400 = 0

    for i in range(1, 13):
        rate = read_positive_real_value(f"Enter the exchange rate for week {i}: ")
        exchange_rates.append(rate)

        if rate < 400:
            count_below_400 += 1

    print("\nExchange rates for the quarter:")
    for i, rate in enumerate(exchange_rates, start=1):
        print(f"Week {i}: {rate} HUF")

    print(f"\nNumber of times the exchange rate was below 400 HUF during the quarter: {count_below_400}")
