# problem : given an array of integers arr[] and an integer K, find the 1st -ve number in every contiguous 
#           subarray(window) of size K. if window does not contain a -ve number, store 0 for that window.

def first_negitive_number_window(arr,k):
    "brute force solution : in every window,looped for 1st negitive number"
    answer = []
    left = 0
    for right in range(k-1,len(arr)):
        add = 0
        for i in range(left,right+1):
            if arr[i]<0:
                add = arr[i]
                break      
        left += 1
        answer.append(add)
    return answer

def first_negitive_number_window2(arr,k):
    n=len(arr)
    answer = []
    indexes = [] # to store the indexes of negitive integers
    # initilize 1st window
    for i in range(k):
        if arr[i] < 0:
            indexes.append(i)
    if indexes:
        answer.append(arr[indexes[0]])
    else:
        answer.append(0)
    left = 1
    for right in range(k,n):
        if indexes and left > indexes[0]:
            indexes.pop(0)
        if arr[right] < 0:
            indexes.append(right)
        if indexes:
            answer.append(arr[indexes[0]])
        else:
            answer.append(0)
        left += 1
    return answer

        


arr=[12,-1,-7,8,-15,30,16,28]
k=3
print(first_negitive_number_window2(arr,k))
