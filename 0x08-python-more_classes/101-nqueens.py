#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in a non-attacking positions
"""


import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, N, solutions)
    return solutions

def solve(board, row, N, solutions):
    if row == N:
        # Found a solution, convert the board to a string representation
        solution = [''.join(row) for row in board]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen at position (row, col)
            board[row][col] = 'Q'

            # Recursively solve for the next row
            solve(board, row + 1, N, solutions)

            # Backtrack and remove the queen from position (row, col)
            board[row][col] = '.'

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == '__main__':
    main()
