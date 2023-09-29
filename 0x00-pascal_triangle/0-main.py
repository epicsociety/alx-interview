#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
pascal_practice = __import__('1-pascal_practice').pascal_practice
test = __import__('test').pascal_tri

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
    print_triangle(pascal_practice(6))
    print_triangle(test(5))
