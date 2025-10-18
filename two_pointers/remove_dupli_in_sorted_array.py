# problem : Given a sorted array, remove duplicates in-place such that each element appears only once.
# Input: [1, 1, 2, 2, 3]  
# Output: [1, 2, 3]
def removeDuplicates(nums):
    left = 0
    for right in range(1,len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
            
    return nums[:left+1]


print(removeDuplicates([1,1,2,2,2,2,2,2,2,2,2,3]))