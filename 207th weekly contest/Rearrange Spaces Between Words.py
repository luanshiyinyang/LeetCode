class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_space = sum(c == ' ' for c in text)
        words = text.split()
        if len(words) == 1:
            return words[0] + (' ' * num_space)
        inner_space = num_space // (len(words) - 1)
        end_space = num_space % (len(words) - 1)
        return (' ' * inner_space).join(words) + (' ' * end_space)


print(Solution().reorderSpaces("a"))