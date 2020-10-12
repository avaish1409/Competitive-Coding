# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def fun(self, s):
        val = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if val[s[i]] > val[s[i-1]]:
                res *= -1
            res += val[s[i]]
            # print(res)
        return res
    
    def romanToInt(self, s: str) -> int:
        val = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arr=[]
        curr=s[0]
        res = 0
        for i in range(1,len(s)):
            if val[s[i]]>val[s[i-1]]:
                curr += s[i]
            else:
                arr.append(curr)
                curr = s[i]
        arr += [curr]
        for i in arr:
            res += self.fun(i)
        return res
