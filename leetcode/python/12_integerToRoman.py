# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        val = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1:'I'}
        for i in val:
            if i <= num:
                res += val[i]*(num//i)
                num %= i
        return res
        
