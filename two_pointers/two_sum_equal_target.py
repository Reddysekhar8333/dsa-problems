# problem : Given a sorted array of positive numbers and a target sum, 
#           find if a pair exists whose sum equals the target.
# Input : [1, 2, 3, 4, 6], target = 6  
# Output: True (Pair: 2 + 4)

def Two_sum_equal_target(arr,target):
    left = 0
    right = len(arr) - 1
    while left < right :
        if arr[left]+arr[right] == target:
            return True
        elif arr[left]+arr[right] < target:
            left += 1
        else:
            right -= 1
    return False
        

print(Two_sum_equal_target([1, 2, 3, 4, 6],6))