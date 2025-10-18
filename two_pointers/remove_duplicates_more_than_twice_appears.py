# problem : Given a sorted array, remove duplicates in-place such that each element appears more than twice.
# input : [1, 1, 1, 2, 2, 3]
# output: [1,1,2,2,3]

def removeDuplicates(arr):
    left = 0
    for right in range(len(arr)):
        if left < 2 or arr[right] != arr[left-2]:
            arr[left] = arr[right]
            left += 1
    return arr[:left]

print(removeDuplicates([1,1,1,1,1,2,2,3,3,3,3]))