def insertionSort(arr):
    # pass
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    arr2= [20,18,12,8,5,-2]
    arr3 = [5,12,7,5,5,7]
    arr4 = [2,3,5,7,13,11]
    print(insertionSort(arr4))

