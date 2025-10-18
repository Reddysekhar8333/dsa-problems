# Check if a string is a palindrome ignoring cases and symbols. (leetcode 125)
# palindrome = sequence of characters that reads the same backward as forward, such as "radar" or "level."

def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())  # '<seperator>'.join() 
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
