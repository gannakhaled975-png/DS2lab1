def selection_sort(arr):
    n=len(arr)
    for i in range (n-1):
        min=arr[i]
        minindex=i
        for j in range (i+1,n):
            if arr[j]<min:
                minindex=j
                min=arr[j]
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr
