# problem : find maximum sum of subarray of size k.

def max_sum_sub_array(arr,k):
    window = 0
    left = 0
    for i in range(k):
        window += arr[i]
    max_sum_k = window
    for right in range(k,len(arr)):
        window = (window-arr[left])+arr[right]
        max_sum_k = max(max_sum_k,window)
        left +=1
    return max_sum_k

k=3
array=[2,1,5,1,3,2]
print(max_sum_sub_array(array,k))