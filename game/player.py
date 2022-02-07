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
      Returns true if guessed, returns false if not
      If the letter was not guessed, it adds it to the list of guessed letters

    Args:
      Guess: The letter passed as a string      
    '''
    was_guessed = False
    for i in self._player_guesses:
      # print(f'letter: {i}')
      if i != guess:
        continue
      elif i == guess:
        print('already guessed')
        was_guessed = True
        break
    
    if was_guessed == False:
      self._player_guesses.append(guess)

    return was_guessed