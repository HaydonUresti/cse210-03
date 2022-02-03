class Player:
  def __init__(self):
    '''Creates an instance of Player
    
    Args: 
        self (Player): An instance of Player
    '''

    self._player_guesses = []

  # def get_guesses(self):
  #   return self._player_guesses

  def is_guessed(self, guess):
    '''Checks if a letter has already been guessed by the user

    Args:
      Guess: The letter passed as a string
    '''
    for i in self._player_guesses:
      print(i)
      if i == guess:
        return True
      else:
        self._player_guesses.append(guess)