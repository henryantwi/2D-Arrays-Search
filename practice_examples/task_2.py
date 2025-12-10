our_arr = [1, 2, 3, 4, 5, 6, 7, 8,..., 100]


def binary_search(arr: list[int], target: int) -> tuple[int, int]:
    left = 0  # Start of search area
    right = len(arr) - 1  # End of search area
    steps = 0  # Count our comparisons

    while left <= right:
        steps += 1  # Count this comparison
        mid = (left + right) // 2  # Find the MIDDLE 50

        if arr[mid] == target:  # Found it!
            return mid, steps
        elif arr[mid] < target:  # Target is HIGHER
            left = mid + 1  # Search RIGHT half
        else:  # Target is LOWER
            right = mid - 1  # Search LEFT half

    return -1, steps  # Not found



def linear_search(arr: list[int], target: int) -> tuple[int, int]:
    """
    Linear Search: Check one by one from the start (slow way!)
    """
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps


# Create array 1 to 100
array_100 = list(range(1, 101))
our_target = 42

# Binary Search
binary_idx, binary_steps = binary_search(array_100, our_target)
print(f"Binary Search for {our_target}:")
print(f"  Found at index: {binary_idx}")
print(f"  Steps: {binary_steps}")

# Linear Search (for comparison)
# linear_idx, linear_steps = linear_search(array_100, our_target)
# print(f"\nLinear Search for {our_target}:")
# print(f"  Found at index: {linear_idx}")
# print(f"  Steps: {linear_steps}")
#
# print(f"\nDifference: {linear_steps - binary_steps} fewer steps with Binary Search!")
