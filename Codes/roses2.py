
def findLengthOfLCIS(nums):
    ans = anchor = flag = 0
    for i in range(len(nums)):
        if i and nums[i-1] >= nums[i]:
            if flag < 1 and nums[i+1] > nums[i] > nums[i-2]:
                flag = 1
            else:
                anchor = i
                flag = 0
            print(anchor, i, flag)
        print(anchor, i, nums[anchor:i])
        ans = max(ans, i - anchor)
    print(ans)
s = input()
l = input()
l = l.split()
for i in range(len(l)):
    l[i] = int(l[i])
findLengthOfLCIS(l)