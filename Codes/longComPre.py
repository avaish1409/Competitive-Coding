class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        pre = ""
        n = len(min(strs, key = len))
        strs.sort(key = len)
        print(strs)
        for i in range(n):
            for j in range(len(strs)):
                print(strs[j][i])
                if strs[j][i] != strs[0][i]:
                    print("here")
                    return pre
            pre += strs[0][i]
        return pre

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
