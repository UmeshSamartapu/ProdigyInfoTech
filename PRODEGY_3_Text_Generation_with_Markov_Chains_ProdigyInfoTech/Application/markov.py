# markov.py

import random
from collections import defaultdict

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.model = defaultdict(list)

    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.order):
            key = tuple(words[i:i+self.order])
            next_word = words[i + self.order]
            self.model[key].append(next_word)

    def generate(self, max_words=50):
        if not self.model:
            return ""
        start = random.choice(list(self.model.keys()))
        result = list(start)
        for _ in range(max_words - self.order):
            key = tuple(result[-self.order:])
            next_words = self.model.get(key)
            if not next_words:
                break
            result.append(random.choice(next_words))
        return ' '.join(result)
