def selection_sort(arr):
    
    for i in range(len(arr)):
        minimum = 10**10
        for j in range(i,len(arr),1):
            if arr[j] < minimum:
                minimum = arr[j]
                min_index = j
        arr[i],arr[min_index] = minimum, arr[i]
        
    return arr