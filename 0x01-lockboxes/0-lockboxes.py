#!/usr/bin/python3
"""
an interview question of dealing with a list of lists
"""


def concat(boxesList, indexList):
    """
    concatenates the lists
    specified by the indices in indexlist from the boxeslist
    """
    KeysList = []
    for j in indexList:
        if j < len(boxesList):
            KeysList += boxesList[j]
    return KeysList


def canUnlockAll(boxes):
    """
    check if a key for each box is contained in any of the boxes
    function takes boxes, a list of lists
    return: bool
    """

    index = 0
    keysForBoxes = list(set(boxes[0]) | {0})
    opened = True

    while opened:
        opened = False
        for i in concat(boxes, keysForBoxes[index:]):
            if i not in keysForBoxes:
                keysForBoxes.append(i)
                index += 1
                opened = True

    return len(boxes) == len(keysForBoxes)
