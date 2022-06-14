# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        if head:
            temp = head
            while temp:
                l.append(temp.val)
                temp = temp.next
            l = sorted(l)
            temp = head
            for l_ in l:
                temp.val = l_
                temp = temp.next
        return head