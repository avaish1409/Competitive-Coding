# 2. Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(l1.val + l2.val)
        root = l3
        if l3.val > 9:
            carry = 1
            l3.val %= 10
        else:
            carry = 0
        while(l1.next or l2.next):
            x = carry
            if l1.next:
                l1 = l1.next
                x += l1.val
            if l2.next:
                l2 = l2.next
                x += l2.val
            if x > 9:
                x %= 10
                carry = 1
            else:
                carry = 0
            l3.next = ListNode(x)
            l3 = l3.next
        if carry == 1:
            l3.next = ListNode(1)
        return root
