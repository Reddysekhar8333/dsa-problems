# problem : continuous subarray sum divisible by k -> leetcode 523
# Given  : array nums and integer k
# return : True if there exists a subarray of length >= 2 such that the sum is divisible by k.

def checkSubarraySum(nums: list[int], k: int) -> bool:
        prefix_map = {0:-1}
        length = 0
        prefixSum = 0
        for i,num in enumerate(nums):
            prefixSum += num
            mod = prefixSum % k
            print(prefix_map)
            if mod in prefix_map:
                length = i - prefix_map[mod]
                if length >= 2:
                    return True
            # prefixSum in map
            if mod not in prefix_map:
                prefix_map[mod] = i
        return False

nums = [1,1,1,1,1,1]
k=6
print(checkSubarraySum(nums,k))