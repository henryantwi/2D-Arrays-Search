def linear_search(arr, target):
    """Check each element one by one until we find the target"""
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps  # Return index and step count
    return -1, steps  # Not found

# Example
numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
target = 30
index, steps = linear_search(numbers, target)
print(f"Array: {numbers}")
print(f"Looking for: {target}")
print(f"Found at index: {index}")
print(f"Steps taken: {steps}")
