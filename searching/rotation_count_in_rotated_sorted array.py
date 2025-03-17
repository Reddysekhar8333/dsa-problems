"""consider an array of distinct numbers sorted in increasing order."""
#the array has been rotated(clockwise) k numbers of times.
#given such an array ,find the value of k.
#ex:-[15,18,2,3,6,12]

def find_rotations(arr):
    k=0 #number of rotations
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]>arr[mid+1]:
            left=mid+1
        else:
            right=mid
    k=left
    return k

nums=[3, 4, 5, 1, 2]
print(find_rotations(nums))
