"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
Sample Output
[-1, 11]
"""
import pytest

def two_number_sum(arr, target):
    """Takes an array and target sum and return a pair of elements from that array
    that sum to the target.

    Args:
        arr (list): array of elements
        target (int): target sum
    """
    # lookup that keeps track of already tracked elements
    lookup = { arr[0]: True }
    
    for element in arr[1:]:
        diff = target - element
        if diff in lookup:
            return [ element, diff ]
        lookup[element] = True
        
    return []


@pytest.mark.parametrize("arr, target, expected_result", [
    ([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11]),
    ([-1, -2, -3], -5, [-3, -2]),
    ([0,0,0,0,0,0,0], 0, [0, 0])
])
def test_two_number_sum(arr, target, expected_result):
    """Test with an non-empty array of distinct integers and a target
    """
    assert two_number_sum(arr, target) == expected_result