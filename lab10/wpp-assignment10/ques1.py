import numpy as np

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i, col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i, j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i, j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row, col] = 1  # Place the queen
            if solve_n_queens(board, row + 1, n):  # Solve for the next row
                return True
            board[row, col] = 0  # Backtrack if needed

    return False

def main():
    n = 8  # Size of the chessboard
    board = np.zeros((n, n), dtype=int)

    if solve_n_queens(board, 0, n):
        print("Solution to the 8-queen problem:")
        print(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
