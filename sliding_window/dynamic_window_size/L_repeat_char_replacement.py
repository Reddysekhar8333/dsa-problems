# problem : you are given a string 's' and an integer 'k'.you can choose any character of the string and
#           change it to any other uppercase english character.you can perform this operation at most 'k' times.
#           return length of longest substring containing the same letter you can get after performing the above operations.
s="REDDY" # many test cases like this   (leetcode 424)  --> "Deepti Talesra youtube"
k=1
def characterReplacement(s,k):
    left = 0
    max_len = 0
    majority = 0
    counts={}

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right],0) + 1
        majority = max(majority,counts[s[right]])

        while (majority + k) < (right-left+1):
            counts[s[left]] -= 1
            left += 1
        max_len = max(max_len,right-left+1)

    return max_len


print(characterReplacement(s,k)) 