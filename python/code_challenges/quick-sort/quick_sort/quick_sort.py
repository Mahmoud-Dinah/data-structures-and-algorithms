def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end :
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if(start < end):
            arr[start], arr[end] = arr[end],arr[start]

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quick_sort(start,end,arr):
    if(start < end ):
        p = partition(start,end,arr)


        quick_sort(start, p - 1, arr)
        quick_sort(p + 1, end, arr)
    return arr

if __name__ == "__main__":
    arr = [2,3,5,7,13,11]
    print (quick_sort(0, len(arr) - 1, arr))
