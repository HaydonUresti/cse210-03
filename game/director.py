from game.word import Word
from game.jumper import Jumper
from game.terminal_service import TerminalService

class Director:
    def __init__(self) -> None:
        """Initializes a new director

        Args: 
            self (Director): An instance of Director.
        """
        self._is_playing = True
        self.word = Word()
        self.jumper = Jumper()
        self.terminal_service=TerminalService()

    def start_game(self):
        """Starts a new game and holds the game loop

        Args: 
            self (Director): An instance of Director.
        """
        while self._is_playing:
            self._print_word()
            self._print_board()
            self._get_input()
            if self.word.is_not_in_word():
                self.jumper.remove_line()
    
    def _print_word(self):
        """Prints the edited word from word

        Args: 
            self (Director): An instance of Director.
        """
        self.terminal_service.write_text(self.word)
        pass

    def _print_board(self):
        """Prints the edited board from jumper

        Args: 
            self (Director): An instance of Director.
        """
        self.terminal_service.write_text(self.jumper)
        pass

    def _get_input(self):
        """Gets player input and sends it to word

        Args: 
            self (Director): An instance of Director.
        """
        _input = self.terminal_service.read_text('Guess a letter [a-z]: ')
        self.word.process_guess(_input)

    def _check_judge(self):
        """Will check if the player has won or lost yet

        Args: 
            self (Director): An instance of Director.
        """
        self._is_playing = self.jumper.is_alive()
        if(self.word.is_finished()):
            self.terminal_service.write_text('You Win!')
            self._is_playing = False