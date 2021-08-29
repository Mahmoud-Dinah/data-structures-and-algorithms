def insertionSort(arr):
    # pass
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    arr2= [20,18,12,8,5,-2]
    # print(insertionSort(arr))
    insertionSort(arr2)
    for i in range(len(arr2)):
        print ("% d" % arr2[i])
