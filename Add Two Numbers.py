# -*-coding:utf-8 -*-
'''
这里使用外部类定义链表会submit报错
'''


class Solution:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            carry = 0
            ret = ListNode(0)
            ret_Last = ret

            while (l1 or l2):
                sum = 0
                if (l1):
                    sum = l1.val
                    l1 = l1.next
                if (l2):
                    sum += l2.val
                    l2 = l2.next
                sum += carry
                ret_Last.next = ListNode(sum % 10)
                ret_Last = ret_Last.next
                carry = (sum >= 10)
            if (carry):
                ret_Last.next = ListNode(1)
            ret_Last = ret.next
            del ret
            return ret_Last
