#!/usr/bin/python3
"""
backtracking N queens
"""

import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] == row - col + i or \
           board[i] == row + col - i:
            return False
    return True


def print_solution(board):
    """ print the solution"""
    print([[i, j] for i, j in enumerate(board)])


def solve_n_queens(board, col):
    """ solve the n queens"""
    global solutions
    if col >= N:
        solutions.append(board.copy())
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_n_queens(board, col + 1)


def main(N):
    """ the main function """

    board = [-1 for _ in range(N)]
    solve_n_queens(board, 0)

    if solutions:
        for solution in solutions:
            print_solution(solution)


if __name__ == "__main__":

    global N, solutions

    solutions = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    main(N)
