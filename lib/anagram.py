class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [candidate for candidate in word_list if self._is_anagram(candidate)]

    def _is_anagram(self, candidate):
        return sorted(candidate.lower()) == sorted(self.word) and candidate.lower() != self.word
