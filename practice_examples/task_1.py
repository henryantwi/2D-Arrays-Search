def diagonal_sum(matrix: list[list[int]]) -> int:
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


