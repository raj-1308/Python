import matplotlib.pyplot as plt
import random

def plot_max_min(total_numbers):
    # Generate random numbers
    numbers = [random.randint(1, 100) for _ in range(total_numbers)]

    # Find max and min
    max_value = max(numbers)
    min_value = min(numbers)

    # Dictionary with keys 'maximum' and 'minimum'
    result = {
        'maximum': max_value,
        'minimum': min_value
    }

    # Plotting the numbers
    plt.figure(figsize=(10, 5))
    plt.plot(numbers, marker='*', linestyle='-', color='blue', label='Values')
    plt.scatter(numbers.index(max_value), max_value, color='red', label='Maximum', zorder=5)
    plt.scatter(numbers.index(min_value), min_value, color='green', label='Minimum', zorder=5)
    plt.title('Maximum and Minimum Finder')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print result
    print(result)

# Example usage
plot_max_min(10)  # Replace 10 with any number you want as start[*]
