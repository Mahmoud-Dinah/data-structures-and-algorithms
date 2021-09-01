from quick_sort.quick_sort import *


def test_Reverse_sorted():
    arr = [20,18,12,8,5,-2]
    assert quick_sort(0, len(arr) - 1, arr) == [-2, 5, 8, 12, 18, 20]

def test_Few_uniques():
    arr = [5,12,7,5,5,7]
    assert quick_sort(0, len(arr) - 1, arr) == [5, 5, 5, 7, 7, 12]

def test_Nearly_sorted():
    arr = [2,3,5,7,13,11]
    assert quick_sort(0, len(arr) - 1, arr) == [2, 3, 5, 7, 11, 13]

