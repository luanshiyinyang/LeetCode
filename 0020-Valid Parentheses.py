class Solution:
    def isValid(self, s: str) -> bool:
        """
        此题有两个关键点：１是顺序２是类型
        利用栈来匹配是最快的
        :param s:
        :return:
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            # 遇到右部判断是否匹配，不匹配则返回False，匹配则向后移动，但是一定有出栈操作
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True



print(Solution().isValid("()"))