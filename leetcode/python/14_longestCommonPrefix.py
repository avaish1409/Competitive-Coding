# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        n = len(min(strs, key = len))
        strs.sort(key = len)
        for i in range(n):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return pre
            pre += strs[0][i]
        return pre
