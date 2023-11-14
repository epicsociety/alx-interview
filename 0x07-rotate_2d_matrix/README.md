## Rotating a 2\*2 matrix

`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`
assigns the values from the swap_tuple to the elements in the matrix. It effectively swaps the values at positions (i, j) and (j, i) in the matrix effectively performing the in-place transposition.

The value at matrix[j][i] is assigned to matrix[i][j].
The value at matrix[i][j] is assigned to matrix[j][i].

The next step is to reverse the rows
