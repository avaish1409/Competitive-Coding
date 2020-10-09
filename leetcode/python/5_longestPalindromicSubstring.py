# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

def expand_and_count(s, start, end):
    while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
        start -= 1
        end += 1
        
    # The indices used for the below substring are:
    # start + 1: because we kept decreasing start by 1 before breaking the loop
    # end: because we kept increasing end by 1 before breaking the loop
    # and python substring excludes the end index
    return s[start + 1 : end]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        
        for i in range(len(s)):
            # If palindrom starts with same index and expands
            # on both sides, it has odd number of letters
            odd = expand_and_count(s, i, i)
            # If palindrom starts with consecutive indices and expands
            # on both sides, it has even number of letters
            even = expand_and_count(s, i, i + 1)
            
            longer = ''
            
            if len(even) > len(odd):
                longer = even
            else:
                longer = odd
                
            if len(longer) > len(longest):
                longest = longer
                
        return longest
