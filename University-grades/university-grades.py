def calculate_average(grades):
    total_grades = sum(grades)
    return total_grades / len(grades)

def calculate_scholarship(average):
    if average < 3.5:
        return 0
    elif 3.5 <= average <= 4.0:
        return 5000
    elif 4.1 <= average <= 4.5:
        return 10000
    elif 4.6 <= average <= 5.0:
        return 15000

def main():
    num_exams = 6
    grades = []
    for i in range(num_exams):
        try:
            grade = float(input(f"Enter grade {i+1}: "))
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid grade.")

    average = calculate_average(grades)
    print(f"Academic average: {average:.2f}")
    scholarship_amount = calculate_scholarship(average)
    print(f"Monthly scholarship: {scholarship_amount} HUF")

if __name__ == "__main__":
    main()
