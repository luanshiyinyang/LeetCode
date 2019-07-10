# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        count = 0
        while curr != None and count != k:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                count -= 1
                temp = head.next
                head.next = curr
                curr = head
                head = temp
            head = curr
        return head