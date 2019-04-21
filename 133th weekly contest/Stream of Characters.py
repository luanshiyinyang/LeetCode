from collections import defaultdict


class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = ''
        self.refer_dict = defaultdict(set)
        for w in words:
            self.refer_dict[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.history += letter
        return any(self.history.endswith(w) for w in self.refer_dict[letter])