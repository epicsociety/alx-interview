#!/usr/bin/python3
"""
pascal's triangle
"""
# n = 5
def pascal_triangle(n):


    c = 1

    for i in range(n):
        if i == 0:
            print(c)
        for j in range(i + 1):
            if (j == 0 or j == i):
                print(c)
            print((i -1)(j) + (i -1)(j+1))
        print()