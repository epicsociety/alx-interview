## Print a list of lists of integers representing the pascal's trinagle

It is simple:

- declare the list of lists and initialize with the first row
- You are working with two loops, the outer one runs from i to n
- the inner loop runs from j to i

- everytime before entering the inner loop, you should initialize the small list (row if you may) with 1 and always end loop by appending a 1 to the row

- the innnermost functionality is the backbone

- always remember you are dealing with a list of lists

- so list_of_lists[i-1][j-1] + list_of_lists[i-1][j] give you the inner summations

- Do not forget to append the small list to the list of lists
