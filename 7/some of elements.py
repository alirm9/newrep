def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program
my_numbers = [5, 12, 8, 3, 21]
result = sum_list(my_numbers)

print(f"Original list: {my_numbers}")
print(f"Sum of numbers: {result}")