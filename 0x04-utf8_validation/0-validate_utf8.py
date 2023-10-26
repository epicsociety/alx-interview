#!/usr/bin/python3
"""
UTF-8 Validation
"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Return True ifa data is valid UTF-8
    or False if not
    Params:
    Data: a list of ints
    """
    def is_start_byte(byte):
        """
        checks if a given byte is a valid
        """
        return (byte >> 6) != 0b10

    # Initialize a counter to keep track of expected following bytes
    expected_following = 0

    for byte in data:
        # Extract the 8 least significant bits
        byte = byte & 0xFF

        if expected_following > 0:
            # If we're expecting following bytes
            if (byte >> 6) != 0b10:
                return False
            expected_following -= 1
        else:
            if byte >> 7 == 0:
                # Single byte character
                expected_following = 0
            elif byte >> 5 == 0b110:
                # Two byte character
                expected_following = 1
            elif byte >> 4 == 0b1110:
                # Three byte character
                expected_following = 2
            elif byte >> 3 == 0b11110:
                # Four byte character
                expected_following = 3
            else:
                return False

    return expected_following == 0
