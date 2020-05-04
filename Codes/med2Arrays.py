import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        med1 = 0
        med2 = 0
        x = (len(nums1) + len(nums2)) % 2
        or1 = nums1
        or2 = nums2
        if nums1 == []:
            if x == 1:
                return nums2[len(nums2) // 2]
            else:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
        elif nums2 == []:
            if x == 1:
                return nums1[len(nums1) // 2]
            else:
                return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2

        while (len(nums1) + len(nums2) > 2):
            med1 = len(nums1) // 2
            med2 = len(nums2) // 2
            if nums1 == [] or nums2 == []:
                break
            if nums1[med1] < nums2[med2]:
                nums1 = nums1[med1:]
                nums2 = nums2[:med2]
            else:
                nums1 = nums1[:med1]
                nums2 = nums2[med2:]
        if x == 0:
            return sum(nums1 + nums2) / len(nums1 + nums2)
        idx = 0
        n1 = 0
        n2 = 0
        try:
            idx += or1.index(nums1[0])
            n1 = nums1[0]
        except:
            return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2]) / 2
        try:
            idx += or2.index(nums2[0])
            n2 = nums2[0]
        except:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2]) / 2
        if idx % 2 == 0:
            return max(n1, n2)
        else:
            return min(n1, n2)


s= Solution()
print(s.findMedianSortedArrays([3],[1,2,4]))