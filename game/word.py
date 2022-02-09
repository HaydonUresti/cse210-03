import random
from game.player import Player
class Word:

   def __init__(self):
       self._not_in_word = False
       self.word_list = ['contradiction', 'instinct', 'professor']
       self._selected_word = self.convert_to_list(self.select_word())
       self._blank_word = self.convert_to_list('_' * len(self._selected_word))
       self.player = Player()
       self._word_finished = False
   
   def select_word(self):
       return random.choice(self.word_list)

   def _to_string(self, list) -> str:
       string = ''
       for letter in list:
           string += (letter+' ')
       return str(string)

   def get_letters(self, guess):
        if guess in self._selected_word:
            self._not_in_word=True
            index = -1
            for item in self._selected_word:
                index += 1
                if item == guess:
                    item = guess
                    self._blank_word.pop(index) 
                    self._blank_word.insert(index, guess)
                    if item == 'c':
                      print('Here be "c"')
        else:
            self._not_in_word=False
            return self._to_string(self._blank_word)

   def process_guess(self, guess):
        self.player.is_guessed(guess)
        self.get_letters(guess)

   def is_not_in_word(self) -> bool:
       return self._not_in_word

   def __str__(self) -> str:
        return self._to_string(self._blank_word)
    
   def convert_to_list(self, string):
        list1=[]
        list1[:0]=string
        return list1

   def is_finished(self) -> bool:
        return self._word_finished
