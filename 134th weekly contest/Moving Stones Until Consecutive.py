# -*-coding:utf-8-*-
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """
        此题的关键在于如何理解最大最小次数
        这里最大次数可以理解为每次尽量小且不交叉的移动，即max_turn = max(a, b, c) - min(a, b, c) - 2（最后减去2是因为有两个位置是位置而不是移动）
        本题的难点是最小次数
            其实最小次数最大就是2，因为你总是可以通过至多两步将两边移动到中间，但是有两个例外
                第一个，三个位置中有两个差为2或者1，那么只需要将另一个插入两者中间即可 这时，最小次数是1
                第二个，三个位置最初连接， 此时最小次数为0，这可以通过最大次数来判断
        """
        max_turn = max(a, b, c) - min(a, b, c) - 2
        min_turn = 2 if min(abs(a-b), abs(b-c), abs(a-c), 3) == 3 else 1
        if max_turn == 0:
            min_turn = 0
        return [min_turn, max_turn]