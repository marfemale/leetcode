# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = ListNode(next = head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        while head and pre:
            tmp = head.next
            head.next = pre
            tmp2 = pre.next
            pre.next = tmp
            head = head.next.next
            pre = tmp2
