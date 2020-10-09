# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if len(str) == 0:
            return 0
        flag = 1
        if str[0]=='+':
            str = str[1:]
        elif str[0]=='-':
            str = str[1:]
            flag=-1
        num = ''
        for i in str:
            if i.isnumeric():
                num += i
            else:
                break
        if num == '':
            return 0
        try:
            num = int(flag) * int(num)
            if num < -1*2**31:
                return -1*2**31
            if num>=2**31:
                return -1 + 2**31
            return num
        except:
            return -1*2**31
            
# Contributor: Anirudh Vaish (avaish1409)
