# A 2D array is like a table with rows and columns
# index[row][column]
matrix = [
   # 0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

print("Our 3x3 matrix:")
for row in matrix:
    print(row)

# Accessing elements: matrix[row][column]
print(f"\nElement at row 0, col 1: {matrix[0][1]}")  # Output: 2
print(f"Element at row 2, col 2: {matrix[2][2]}")  # Output: 9

# The diagonal (top-left to bottom-right)
print("\nDiagonal elements:")
for i in range(3):
    print(f"Position [{i}][{i}] = {matrix[i][i]}")
