# problem : given a sorted integer array, return a new array containing the sqares of all numbers,sorted.
# input :[-4,-1,0,3,10]
# output:[0,1,9,16,100]

def squared_sorted_array(arr):
    result = []
    left = 0
    right = len(arr)-1
    while left <= right :
        if arr[left]**2 < arr[right]**2:
            result.insert(0,arr[right]**2)
            right -= 1
        else:
            result.insert(0,arr[left]**2)
            left += 1
    return result

print(squared_sorted_array([-12,-10,-4,-1,0,3,10]))