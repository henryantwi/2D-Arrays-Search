
def find_diagonal(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        print(matrix[i][i])



our_matrix = [
  # 0   1   2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

find_diagonal(our_matrix)
