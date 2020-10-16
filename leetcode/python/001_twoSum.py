# 1. Two Sum Problem (https://leetcode.com/problems/two-sum/)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            if nums[i+1:].count(target-nums[i]) != 0:
                res = [i, 1+i+nums[i+1:].index(target-nums[i])]
                break
        return res
