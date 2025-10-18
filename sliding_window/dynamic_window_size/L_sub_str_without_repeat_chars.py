# problem : Longest substring without repeating characters.
#           given a string s, find the length of the longest substring without repeating characters. (leetcode 3)
def longest_unique_substring(s):
    answer = 0
    left = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        answer = max(answer,(right-left)+1)
    return answer

s="abcabcbbh"
print(longest_unique_substring(s))