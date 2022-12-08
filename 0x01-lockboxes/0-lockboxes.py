#!/usr/bin/python3
"""
Method that determines if
all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    function canUnlockAll
    """
    size_box = len(boxes)
    keys = [0]

    for key in keys:
        for box in boxes[key]:
            if box > size_box:
                return False
            else:
                if box in keys:
                    continue
                else:
                    keys.append(box)

    if size_box == len(keys):
        return True

    return False
