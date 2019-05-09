# -*-coding:utf-8-*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution():
    def swapPairs(self, head):
        """
        这是一道比较简单的题目
        力求代码简洁的解法如下
        a表示当前，b表示后一个那么a，b交换的结果不过是pre->a->b->b.next变为pre->b->a->b.next
        """
        pre, pre.next = ListNode(0), head
        start = pre
        while pre.next and pre.next.next:  # 存在一对才能交换
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return start.next