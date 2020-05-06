# indexes of int adding to a target
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)-1):
            if nums[i+1:].count(target-nums[i]) != 0:
                print(nums[i])
                print(nums[i+1:])
                res = [i, i+nums[i+1:].index(target-nums[i])]
                break
        return res


s= Solution
print(s.twoSum(s,[3, 4], 7))
