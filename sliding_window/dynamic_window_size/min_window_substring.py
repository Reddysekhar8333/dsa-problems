# problem : Given two strings 's' and 't', return the minimum window in 's'    [leetcode 76]
#           which contain all the characters in 't'. If no such window exists, return an empty string "".
# Input: s="adobecodebanc" , t="abc"
# Output: "banc"
def min_window_substring(s,t):
    # step 1: initialize a dict for storing frequency of 't'
    t_dict={}
    for i in t:
        if i in t_dict:
            t_dict[i]+=1
        else:
            t_dict[i]=1
    # step 2: 
    left = 0 # pointers
    char_cnt, total = 0, len(t_dict) # total is unique chars in t
    ans_len=float('inf')
    sub1=0
    for right in range(len(s)):
        char=s[right]
        if char in t_dict:
            t_dict[char]-=1
            if t_dict[char]==0:
                char_cnt +=1

        while left <=right and char_cnt == total:
            char=s[left]
            if char in t_dict:
                t_dict[char] += 1 
                if t_dict[char] > 0:
                    char_cnt -= 1
            if right - left + 1 < ans_len:
                ans_len = right - left + 1
                sub1 = left
            left+=1
   
    return "" if ans_len==float('inf') else s[sub1:sub1+ans_len]
    


print(min_window_substring("adobecodeabanc","aabc"))