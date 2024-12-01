# Data retrieving from a file
with open("input.txt", "r") as file:
    left_column, right_column = [], []
    for line in file:
        numbers = line.strip().split()
        left_column.append(int(numbers[0]))
        right_column.append(int(numbers[1]))
        """
        Part above can be improved like this: 
        a, b = map(int, line.strip().split())
        left_column.append(a)
        right_column.append(b)
        """

# Solution for a puzzle
left_column.sort()
right_column.sort()

total_distance = sum(abs(b - a) for a, b in zip(left_column, right_column))
print(total_distance)

# Part Two Solution
count_sum = 0
for num in set(left_column):
    count_sum += num * right_column.count(num)
"""
Part above can be improved like this: 
right_column_counts = Counter(right_column)
count_sum = sum(num * right_column_counts[num] for num in set(left_column))
"""

print(count_sum)