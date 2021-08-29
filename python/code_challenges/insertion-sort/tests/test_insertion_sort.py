from insertion_sort.insertion_sort import *

def test_insertion_sort():
    arr = [8,4,23,42,16,15]
    assert insertionSort(arr) == [4,8,15,16,23,42]

def test_Reverse_sorted():
    arr = [20,18,12,8,5,-2]
    assert insertionSort(arr) == [-2, 5, 8, 12, 18, 20]

def test_Few_uniques():
    arr = [5,12,7,5,5,7]
    assert insertionSort(arr) == [5, 5, 5, 7, 7, 12]

def test_Nearly_sorted():
    arr = [2,3,5,7,13,11]
    assert insertionSort(arr) == [2, 3, 5, 7, 11, 13]
