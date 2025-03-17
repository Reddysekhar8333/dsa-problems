#bubble sort 
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped = True
        if not swapped:  # If no swaps, the list is already sorted
            break
    return arr
print("OUTPUT:",end=" ")
print(bubble_sort([5,4,3,2,1,0]))