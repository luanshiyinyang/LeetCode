class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def nextLargerNodes(self, head):
        """
        本以为是个dp，没想到是个数据结构技巧
        核心思路就是不断将列表下标入栈，当遇到即将入栈的下标对应的值比栈顶元素大则将栈顶出栈（同时将该下标对应结果赋值为即将入栈元素）
        直到栈为空或者栈顶元素大于即将入栈下标对应元素
        :type head:
        :rtype: List[int]
        """
        number_list = []
        while head.next is not None:
            number_list.append(head.val)
            head = head.next
        number_list.append(head.val)
        # 此时见链表转化为栈
        rst = [0 for i in range(len(number_list))]
        stack = list()
        stack.append(0)
        for i in range(1, len(number_list)):
            if len(stack) > 0:
                if number_list[i] > number_list[stack[len(stack)-1]]:
                    while len(stack) > 0:
                        top = stack.pop()
                        if number_list[top] < number_list[i]:
                            rst[top] = number_list[i]
                        else:
                            stack.append(top)
                            break
                    stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return rst
