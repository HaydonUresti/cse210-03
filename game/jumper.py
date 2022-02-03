from xmlrpc.client import Boolean


class Jumper:
    def __init__(self) -> None:
        self._jumper_img = ['  ___ ',
                            ' /___\\',
                            ' \\   /',
                            '  \\ / ',
                            '   o  ',
                            '  /|\\ \n  / \\ \n      \n^^^^^^^']
        self._alive = True

    def _assemble_jumper(self) -> str:
        _full_jumper=''
        for line in self._jumper_img:
            _full_jumper+= str(line) + '\n'
        return _full_jumper

    def remove_line(self) -> None:
        _line = self._jumper_img.pop(0)
        if _line == '  \\ / ' or _line == '   x  ':
            self._alive = False
            self._jumper_img = ['   x  ',
                                '  /|\\ \n  / \\ \n      \n^^^^^^^']
    
    def is_alive(self) -> bool:
        return self._alive

    def __str__(self) -> str:
        return str(self._assemble_jumper())
