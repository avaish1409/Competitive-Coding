class Solution:
    def kLengthApart(self, nums: [int], k: int):
        i = nums.index(1)
        while i < len(nums):
            # print(i, end=' ')
            for j in range(i+1, len(nums)):
                # print(j)
                if nums[j] == 1:
                    if j - i > k:
                        i = j - 1
                        break
                    else:
                        print(i, j)
                        return False
            i += 1
        return True


s = Solution()
print(s.kLengthApart([1,0,0,1,0,1],2))
