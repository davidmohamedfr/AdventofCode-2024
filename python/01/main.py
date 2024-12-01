def calculate_total_distance(input_data):
    # Parse input into two lists
    left_numbers = []
    right_numbers = []

    # Split the input data into pairs and separate them
    for line in input_data.strip().split('\n'):
        left, right = map(int, line.strip().split())
        left_numbers.append(left)
        right_numbers.append(right)

    # Sort both lists
    left_numbers.sort()
    right_numbers.sort()

    # Calculate distances between corresponding pairs
    total_distance = 0
    for left, right in zip(left_numbers, right_numbers):
        distance = abs(left - right)
        total_distance += distance

    return total_distance


# Process the input data
with open('input', 'r') as file:
    input_data = file.read()

result = calculate_total_distance(input_data)
print(f"Total distance: {result}")