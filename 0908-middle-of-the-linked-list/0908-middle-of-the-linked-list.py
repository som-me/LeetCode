# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        #To solve this problem we have another method - FAST and SLOW pointers
        fast, slow = head, head
        res = list()
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow