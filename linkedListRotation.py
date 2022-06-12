# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        size = 1
        temp = head
        while temp:
            temp = temp.next
            size+=1

        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        if k>len(l):
            k = int(k%len(l))
        if len(l)>0:
            l_ = (l[-k:] + l[:-k])
            temp = head
            i = 0
            while i<=len(l_)-1:
                head.val = l_[i]
                head = head.next
                i+=1
            head = temp
            while temp:
                temp = temp.next
        return head