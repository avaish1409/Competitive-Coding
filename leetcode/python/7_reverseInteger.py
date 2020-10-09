# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x<0:
            flag = -1
            x = abs(x)
        s1 = str(x)
        s2 = s1[::-1]
        try:
            y = int(s2)*flag
            if y>(-1+(2**31)) or y<(-1*(2**31)):
                return 0
            return y
        except:
            return 0
        
# Contributor: Anirudh Vaish (avaish1409)
