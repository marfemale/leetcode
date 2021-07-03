# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for i, sub in enumerate(lists):
            if sub:
                heapq.heappush(q, (sub.val, i))
        dummy = cur = ListNode()
        while q:
            mins = heapq.heappop(q)
            cur.next = lists[mins[1]]
            cur = cur.next
            lists[mins[1]] = cur.next
            if cur.next:
                heapq.heappush(q, (cur.next.val, mins[1]))
        return dummy.next
