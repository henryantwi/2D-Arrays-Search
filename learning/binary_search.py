def binary_search(arr, target):
    """Divide and conquer: keep cutting the search area in half"""
    steps = 0
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1, steps

# Example (must be sorted!)
sorted_numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
target = 30
index, steps = binary_search(sorted_numbers, target)
print(f"Array: {sorted_numbers}")
print(f"Looking for: {target}")
print(f"Found at index: {index}")
print(f"Steps taken: {steps}")
