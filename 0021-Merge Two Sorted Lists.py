# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        本题主要是对两个有序链表的合并，只要抓住核心：用两个指针遍历两个链表将较小者放入新的结果中即可
        至于循环还是递归不过是编码技巧罢了
        """
        rst = ListNode(-1)
        current = rst
        while(l1 and l2):
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return rst.next
