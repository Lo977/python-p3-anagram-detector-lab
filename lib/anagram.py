# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word_letters = word

    def match(self,words):
        return[letters for letters in words if sorted(letters) == sorted(self.word_letters)]
        # match_lits = []

        # for word in words:
        #     if sorted([char for char in word]) == self.word_letters:
        #         match_lits.append(word)
        # return match_lits