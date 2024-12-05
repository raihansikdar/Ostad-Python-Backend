def generate_fibonacci_by_terms(number):
   
    if number <= 0:
        return []
    series = [0, 1]
    while len(series) < number:
        series.append(series[-1] + series[-2])
    return series[:number]

def generate_fibonacci_by_max_value(max_value):
   
    if max_value < 0:
        return []
    series = [0, 1]
    while True:
        next_term = series[-1] + series[-2]
        if next_term > max_value:
            break
        series.append(next_term)
    return series

def get_positive_integer(n):
    while True:
        try:
            value = int(input(n))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            number = get_positive_integer("Enter the number of terms: ")
            series = generate_fibonacci_by_terms(number)
            print(f"Fibonacci series ({number} terms): {', '.join(map(str, series))}")
        
        elif choice == '2':
            max_value = get_positive_integer("Enter the maximum value: ")
            series = generate_fibonacci_by_max_value(max_value)
            print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, series))}")
        
        elif choice == '3':
            print("Goodluck!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


