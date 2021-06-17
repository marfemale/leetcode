# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res, stack = [], []
        for num in arr[::-1]:
            while stack and num >= stack[-1]:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(0)
            stack.append(num)
        return res[::-1]
