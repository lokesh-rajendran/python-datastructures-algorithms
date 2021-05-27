"""
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
[1, 4, 9, 25, 36, 64, 81]
"""
import pytest

def sorted_squared_array(arr):
    """Squares the elements of given array and sorts the squared elements
    in ascending order.

    Args:
        arr (list): given list of elements to be sorted
    """

    squared_list = list(map(lambda x: x*x, arr))
    squared_list.sort()
    return squared_list
    

@pytest.mark.parametrize("arr, expected", [
    ([-7,1,2,3,-1, -2, -3], [1, 1, 4, 4, 9, 9, 49]),
    ([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81])
])
def test_sorted_squared_array(arr, expected):
    assert sorted_squared_array(arr) == expected