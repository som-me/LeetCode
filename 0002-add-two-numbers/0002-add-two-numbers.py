# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        resHead = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            #Here we are checking for any carry if total = 10, 10/10 = 1, so carry 1 will move forward.
            carry = total // 10
            #Here we made a digit variable to store the non carry digit, if total = 7 or 12, 7%10 = 7 or 12%10 = 2. so would have stored 2.  
            digit = total % 10

            resHead.next = ListNode(digit)
            resHead = resHead.next

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        return dummy.next







        