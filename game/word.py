import random
class Word:

   def __init__(self):
       self._selected_word = ""
       self.word_list = ['contradiction', 'instinct', 'professor']
       self._blank_word = ""
   
   def select_word(self):
       return random.choice(self.word_list)

   def get_letters(self, guess):
        _selected_word = self.select_word(self)

        self._blank_word = '_' * len(_selected_word)

        if guess in _selected_word:
            for i in _selected_word:
                if i == guess:
                    self._blank_word = guess
        
        return self._blank_word



   def __str__(self) -> str:
        return f'{self.blank_word}'
