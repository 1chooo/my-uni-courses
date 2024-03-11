def quick_sort(arr, lb, rb) :
    
    if (lb >= rb) :
        return arr

    pivot = arr[rb]
    l = lb
    r = rb - 1

    while True :
        while (arr[l] < pivot) :
            l += 1
        
        while (arr[r] >= pivot and r > lb) :
            r -= 1

        if (l < r) :
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
        else :
            break

    if (arr[rb] != arr[l]) :
        temp = arr[rb]
        arr[rb] = arr[l]
        arr[l] = temp

    quick_sort(arr, lb, l - 1)
    quick_sort(arr, l + 1, rb)
    
    return arr