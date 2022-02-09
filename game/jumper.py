from xmlrpc.client import Boolean


class Jumper:
    def __init__(self) -> None:
        """Initializes a new jumper

        Args: 
            self (Jumper): An instance of Jumper.
        """
        self._jumper_img = ['  ___ ',
                            ' /___\\',
                            ' \\   /',
                            '  \\ / ',
                            '   o  ',
                            '  /|\\ \n  / \\ \n      \n^^^^^^^']
        self._alive = True

    def _assemble_jumper(self) -> str:
        """Assembles the jumper as a list to a string

        Args: 
            self (Jumper): An instance of Jumper.
        """
        _full_jumper=''
        for line in self._jumper_img:
            _full_jumper+= str(line) + '\n'
        return _full_jumper

    def remove_line(self) -> None:
        """Removes a line from the jumper, checks if the jumper has died

        Args: 
            self (Jumper): An instance of Jumper.
        """
        _line = self._jumper_img.pop(0)
        if _line == '  \\ / ' or _line == '   x  ':
            self._alive = False
            self._jumper_img = ['   x  ',
                                '  /|\\ \n  / \\ \n      \n^^^^^^^']
    
    def is_alive(self) -> bool:
        """Will return whether the jumper has died

        Args: 
            self (Jumper): An instance of Jumper.

        Return:
            self._alive (bool): bool of if you are alive or not
        """
        return self._alive

    def __str__(self) -> str:
        """Returns jumper as a string

        Args: 
            self (Jumper): An instance of Jumper.

        Returns:
            jumper_img 
        """
        return '\n'+str(self._assemble_jumper())

    def jumper_win(self) -> str:
        """Returns jumper as a string

        Args: 
            self (Jumper): An instance of Jumper.

        Returns:
            jumper_img 
        """
        self._jumper_img = '  \\o/ \n   |  \n  / \\ \n^^^^^^^'
        return str(self._jumper_img)
