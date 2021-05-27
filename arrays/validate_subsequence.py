"""
Validate Subsequence
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Sample Output
true
"""

import pytest


def validate_subsequence(arr, sequence):
    """Validate if the sequence array is subset of the given arr

    Args:
        arr (list): given arr
        sequence (list): sequnece to validate

    Returns:
        bool: is sequence a subset of the given array
    """
    
    currentSeqIndx = 0
    currentArrIndx = 0
    
    while currentSeqIndx < len(sequence) and currentArrIndx < len(arr):
        if arr[currentArrIndx] == sequence[currentSeqIndx]:
            currentSeqIndx += 1
            
        currentArrIndx += 1
    
    
    return currentSeqIndx == len(sequence)


@pytest.mark.parametrize("arr, sequence, expected", [
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
    ([1,2,3,4,5,6], [1,2,3,4,5,6], True),
    ([1,2,3,4,-1,0,2], [-1], True)
])
def test_validate_subsequence(arr, sequence, expected):
    """Test case """
    
    assert validate_subsequence(arr, sequence) == expected