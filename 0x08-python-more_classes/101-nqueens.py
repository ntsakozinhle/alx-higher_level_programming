#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at the sepcified position.
    """

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, n):
    """
    Solve the N queens problem using backtracing.
    """
    if col >= n:
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0

def print_solution(board, b):
    """
    Print the solution in the required format.
    """
    for i in range(n):
        print("".join(["Q" if board[i][j] == 1 else "." for j in range(n)]))
    print()

def nqueens(n):
    """
    Main function to solve the N queens problem.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at leats 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
