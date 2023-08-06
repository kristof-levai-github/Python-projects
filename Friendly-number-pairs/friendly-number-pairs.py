def read_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def find_divisors_sum(num):
    divisors_sum = 1  # Start with 1 as every number is divisible by 1

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:  # To avoid counting the same divisor twice
                divisors_sum += num // i

    return divisors_sum

def find_friendly_pairs(lower_bound, upper_bound):
    friendly_pairs = []
    for num1 in range(lower_bound, upper_bound + 1):
        div_sum1 = find_divisors_sum(num1)
        if lower_bound <= div_sum1 <= upper_bound:
            div_sum2 = find_divisors_sum(div_sum1)
            if num1 == div_sum2 and num1 != div_sum1:
                pair = (num1, div_sum1)
                if pair not in friendly_pairs:
                    friendly_pairs.append(pair)

    return friendly_pairs

if __name__ == "__main__":
    lower_bound = read_integer("Enter the lower bound of the interval: ")
    upper_bound = read_integer("Enter the upper bound of the interval: ")

    if lower_bound >= upper_bound:
        print("Invalid input. The lower bound must be smaller than the upper bound.")
    else:
        friendly_pairs = find_friendly_pairs(lower_bound, upper_bound)

        if friendly_pairs:
            print("Friendly number pairs:")
            for pair in friendly_pairs:
                print(pair)
        else:
            print("No friendly number pairs found within the specified interval.")
