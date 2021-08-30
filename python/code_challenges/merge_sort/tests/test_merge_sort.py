from merge_sort.merge_sort import *

def test_Reverse_sorted():
   arr = [20,18,12,8,5,-2]
   assert mergeSort(arr) == [-2, 5, 8, 12, 18, 20]

def test_Few_uniques():
    arr = [5,12,7,5,5,7]
    assert mergeSort(arr) == [5, 5, 5, 7, 7, 12]

def test_Nearly_sorted():
    arr = [2,3,5,7,13,11]
    assert mergeSort(arr) == [2, 3, 5, 7, 11, 13]
