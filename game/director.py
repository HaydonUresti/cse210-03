from word import Word
from jumper import Jumper
from terminal_service import TerminalService

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
            self._check_judge()
    
    def _print_word(self):
        """Prints the edited word from word

        Args: 
            self (Director): An instance of Director.
        """
        self.terminal_service.write_text(self.word)
        pass

    def _print_board(self):
        self.terminal_service.write_text(self.jumper)
        pass

    def _get_input(self):
        _input = self.terminal_service.read_number('Guess a letter [a-z]: ')
        self.word.get_letters(_input)

    def _check_judge(self):
        self._is_playing = self.judge.win_or_lose()