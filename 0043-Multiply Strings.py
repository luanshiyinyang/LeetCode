class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        rst = [0 for i in range(len(num1) + len(num2))]
        pos = len(rst) - 1
        for n1 in reversed(num1):
            in_pos = pos
            for n2 in reversed(num2):
                value = int(n1) * int(n2)
                rst[in_pos] += value
                rst[in_pos-1] += rst[in_pos] // 10
                rst[in_pos] %= 10
                in_pos -= 1
            pos -= 1
        place = 0
        while place < len(rst) and rst[place] == 0:
            place += 1
        if place == len(rst):
            return "0"
        else:
            return ''.join(map(str, rst[place:]))