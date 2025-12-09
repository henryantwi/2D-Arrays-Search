

# length(our_mtr) = 3
# n < len(our_mtr)
# range(len(our_mtr)) ie. range(3)( -> (0, 1, 2)


def diagonal_sum(mtr: list[list[int]]) -> int:
    total: int = 0
    for i in range(len(mtr)):
        total = total + mtr[i][i]
    return total


if __name__ == "__main__":
    our_mtr = [
       # 0  1  2
        [3, 2, 8], # 0
        [7, 9, 3], # 1
        [5, 6, 8]  # 2
    ]
    print(diagonal_sum(our_mtr))
    