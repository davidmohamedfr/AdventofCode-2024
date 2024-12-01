def calculate_similarity_score(input_values):
    # Parse input into two lists
    left_numbers = []
    right_numbers = []

    # Split the input data into pairs and separate them
    for line in input_values.strip().split('\n'):
        left, right = map(int, line.strip().split())
        left_numbers.append(left)
        right_numbers.append(right)

    # Count occurrences of each number in the right list
    right_counts = {}
    for num in right_numbers:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate similarity score
    total_score = 0
    for left_num in left_numbers:
        # Get count of this number in right list (0 if not present)
        count_in_right = right_counts.get(left_num, 0)
        score = left_num * count_in_right
        total_score += score

    return total_score


# Process the input data
with open('input', 'r') as file:
    input_data = file.read()

result = calculate_similarity_score(input_data)
print(f"Similarity score: {result}")