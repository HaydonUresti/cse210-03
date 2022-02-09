import random
from game.player import Player
class Word:

   def __init__(self):
       """Initializes a new instance of Word. 
        Args:
            self (Word): An instance of Word
       """
       self._not_in_word = False
       self._word_list = ['contradiction', 'instinct', 'professor', 'trench', 'strategic',
       'overview', 'economics', 'transmission', 'goalkeeper', 'presidential', 'resignation',
       'momentum']
       self._selected_word = self._convert_to_list(self._select_word())
       self._blank_word = self._convert_to_list('_' * len(self._selected_word))
       self._player = Player()
       self._word_finished = False
   
   def _select_word(self):
       """Selects a new word. 
        Args:
            self (Word): An instance of Word
       """
       return random.choice(self._word_list)

   def _to_string(self, list) -> str:
       """Turns the list into a string.
        Args:
            self (Word): An instance of Word
       """
       string = ''
       for letter in list:
           string += (letter+' ')
       return str(string)

   def _get_letters(self, guess):
       """Replaces blank spaces with correct letter.
        Args:
            self (Word): An instance of Word
            guess: the guess the player makes

       """
       if guess in self._selected_word:
            self._not_in_word=False
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
            self._not_in_word=True
            return self._to_string(self._blank_word)

   def process_guess(self, guess):
        """ 
        Args:
            self (Word): An instance of Word
            guess: the guess the player makes
        """
        if not self._player.is_guessed(guess):
            self._get_letters(guess)
            self._check_win()
        else:
            self._not_in_word=False

   def is_not_in_word(self) -> bool:
       """Returns whether or not a guess is in the word. 
        Args:
            self (Word): An instance of Word
       """
       return self._not_in_word

   def __str__(self) -> str:
        """Accesses and returns a string version of the blank word. 
        Args:
            self (Word): An instance of Word
        """
        return self._to_string(self._blank_word)
    
   def _convert_to_list(self, string):
        """ Converts a list to a string 
        Args:
            self (Word): An instance of Word
        """
        list1=[]
        list1[:0]=string
        return list1

   def _check_win(self):
        """Checks for any _ in word. 
        Args:
            self (Word): An instance of Word
        """
        if '_' in self._blank_word:
           return
        else:
            self._word_finished=True

   def is_finished(self) -> bool:
        """A method to return the value of _word_finished. 
        Args:
            self (Word): An instance of Word
        """
        return self._word_finished
