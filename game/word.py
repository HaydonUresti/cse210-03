import random
from game.player import Player
class Word:

   def __init__(self):
       self.word_list = ['contradiction', 'instinct', 'professor']
       self._selected_word = self.select_word()
       self._blank_word = '_ ' * len(self._selected_word)
       self.player = Player()
   
   def select_word(self):
       return random.choice(self.word_list)

   def get_letters(self, guess):
      
        if guess in self._selected_word:
            j=0
            for i in self._selected_word:
                j+=2
                if i == guess:
                    self._blank_word[j] = guess
        
        return self._blank_word

   def process_guess(self, guess):
        self.player.is_guessed(guess)
        self.get_letters(guess)

   def __str__(self) -> str:
        return f'{self._blank_word}'
