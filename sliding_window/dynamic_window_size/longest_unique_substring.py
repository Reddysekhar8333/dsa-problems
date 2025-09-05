# problem : Longest substring without repeating characters.

def longest_unique_substring(s):
    answer = 0
    left = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        temp_ans =(right-left)+1
        answer = max(answer,temp_ans)
    return answer

s="abcabcbb"
print(longest_unique_substring(s))