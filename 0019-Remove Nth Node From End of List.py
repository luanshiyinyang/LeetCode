# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        此题的含义是删除倒数第ｎ个结点
        不清楚暴力解法会不会有问题
        比较常见的思路有移动到最后next为None时停止，反向移动ｎ长度
        也可以设置两个指针，其中一个先右移ｎ长度，然后另一个随着这一个指针移动到这个指针到底的位置，此时另一个指向的就是目标
        :param head:
        :param n:
        :return:
        """
        head0 = ListNode(0)
        head0.next = head
        p1 = p2 = head0
        for i in range(n):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next

        return head0.next
