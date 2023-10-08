#!/usr/bin/python3
"""
an interview question of dealing with a list of lists
"""


def canUnlockAll(boxes):
    """
    check if a key for each box is contained in any of the boxes
    function takes boxes, a list of lists
    return: bool
    """

    keysForBoxes = list(set(boxes[0]) | {0})

    for i in keysForBoxes:
        for j in boxes[i]:
            if j not in keysForBoxes:
                keysForBoxes.append(j)
            else:
                continue
    return len(boxes) == len(keysForBoxes)
