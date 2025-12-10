def linear_search(arr, x):
    step = 0

    for i in range(len(arr)):
        if arr[i] == x:
            return i, step
        else:
            step += 1
    return -1, step


array_100 = list(range(1, 101))
our_target = 42

index, steps = linear_search(array_100, our_target)
print(f"Linear Search for {our_target}:")
print(f"  Found at index: {index}")
print(f"  Steps: {steps}")