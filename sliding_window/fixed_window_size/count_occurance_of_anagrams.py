# problem : given a string "txt" and a string "pat",
#           we need to count how many anagrams of pat are present in "txt" as a substring

def is_anagram(window,pat):
    "helper funtion to count_occurance1()"
    if sorted(window) == sorted(pat):
        return True
    else:
        return False
def count_occurance1(txt,pat):
    " brute force solution "
    result = 0
    left = 0
    for right in range(len(pat),len(txt)+1):
        window = txt[left:right]
        if is_anagram(window,pat):
            result +=1
        left += 1
    return result


def count_occurance2(txt,pat):
    result = 0
    k=len(pat)
    if len(txt) < k:
        return result
    # step 1 : use hashmap
    window_hash , pat_hash = {},{}
    for i in range(k):
        window_hash[txt[i]] = window_hash.get(txt[i],0)+1
        pat_hash[pat[i]] = pat_hash.get(pat[i],0)+1
    if window_hash == pat_hash:
        result+=1
    # step 2 : use the sliding window
    left = 0
    for right in range(k,len(txt)):
        window_hash[txt[left]] -= 1  # here is the chance of a char frequency is 1+ times
        if window_hash[txt[left]] == 0:
            window_hash.pop(txt[left])
        left+=1
        window_hash[txt[right]] = window_hash.get(txt[right],0)+1
        if window_hash == pat_hash:
            result+=1
    return result
    

print(count_occurance2("forxxorfxdofr","for"))