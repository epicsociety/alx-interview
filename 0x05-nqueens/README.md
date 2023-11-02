## Backtracking

Backtracking is a recursive algorithmic technique that incrementally builds candidates for a solution. It explores the search space, discarding candidates that cannot lead to a valid solution. When a dead-end is reached, the algorithm backtracks to the previous state and explores a different path.

### Pseudocode for Backtracking:

```function backtrack(candidate):
    if candidate is a solution:
        return
    for next_candidate in generate_candidates(candidate):
        if is_valid(next_candidate):
            make_choice(next_candidate)
            backtrack(next_candidate)
            undo_choice(next_candidate)
```

## N-Queens Problem

The N-Queens problem is a classic example of a combinatorial problem that can be solved using backtracking. In this problem, you need to place N queens on an NxN chessboard in such a way that no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).

### Pseudocode for N-Queens using Backtracking:

```function solve_n_queens(board, col):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            place_queen(board, i, col)
            if solve_n_queens(board, col + 1):
                return True
            remove_queen(board, i, col)
    return False
```
