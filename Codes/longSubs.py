# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Sliding Window

class Solution:
    def isUnq(self,s):
        for i in range(len(s)):
            if s.count(s[i]) != 1:
                return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        op = 0
        op2 = 0
        print('o o2 i str')
        i = 0
        count =0
        while i + op < len(s):
            if self.isUnq(s[i:i+op2]):
                op2 += 1
                print(op, op2, i, s[i:i+op2])
                i -= 1
            else:
                op = max(op, op2)
                op2 = op
            i += 1
            count += 1
        print('count: ',count)
        return op-1

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """

        str_list = []
        max_length = 0
        count = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]
                count += 1

            str_list.append(x)
            max_length = max(max_length, len(str_list))
            # print(str_list)
        print(count)


        return max_length


s = Solution()
print(s.lengthOfLongestSubstring2('ab'*10 + 'c' + 'ab'*10))