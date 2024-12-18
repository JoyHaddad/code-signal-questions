def insertion_sort(arr):
    # TODO: implement the Insertion Sort algorithm
    for i in range(0, len(arr) - 1, 1):
            j = i
            key = i + 1
            while j >= 0:
                if arr[j] > arr[key]:
                    arr[j], arr[key] = arr[key], arr[j]
                    key = j
                j -= 1
                
    return arr