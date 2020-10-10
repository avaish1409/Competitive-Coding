# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        x2 = 0
        count = 0
        while(x>x2):
            x2 *= 10
            x2 += x%10
            x //= 10
            count += 1
        x3 = x
        while(x3!=0):
            x3//=10
            count -= 1
        if x == x2 or (x==x2//10 and count !=0):
            return True
        return False
