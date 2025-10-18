# compute the prefix sum funtion
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1]+arr[i]
    return prefix

arr = [1, 4, 2, 7, 3]
p = prefix_sum(arr)
print(p)   # [1, 5, 7, 14, 17]
