def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Iterate over the remaining strings
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the current string
        while not string.startswith(prefix):#''' startswith()'''#The substring you want to check at the beginning of the string. It can be a string or a tuple of strings.
            prefix = prefix[:-1]  # Remove the last character from prefix
            if not prefix:  # If prefix becomes empty, return ""
                return ""
    
    return prefix

lis=['rrrhffgjgjkj','rrrhfjg','rrrhghty','rrrhghha']
a=longestCommonPrefix(lis)
print(a)