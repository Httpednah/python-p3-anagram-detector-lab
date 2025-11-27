class Anagram:
    def __init__(self, word):
        # store the word in lowercase to make comparison case-insensitive
        self.word = word.lower()

    def match(self, words):
        # return a list of words from the input that are anagrams of self.word
        matches = []
        sorted_word = sorted(self.word)
        for w in words:
            if sorted(w.lower()) == sorted_word:
                matches.append(w)
        return matches
