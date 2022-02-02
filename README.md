# cse210-03
## Director
- print_word()
- print_board()
- get_input()
- check_judge(win_or_lose)
## Terminal service
- read_text(prompt)
- write(print)
## Player
- previous_guesses
## Word
- word
- select_word()
## Judge
- judge_guess()
- win_or_lose() -> Boolean
## Jumper
- Jumper img
- remove_line()

# Rules
Jumper is played according to the following rules.

- The puzzle is a secret word randomly chosen from a list.
- The player guesses a letter in the puzzle.
- If the guess is correct, the letter is revealed.
- If the guess is incorrect, a line is cut on the player's parachute.
- If the puzzle is solved the game is over.
- If the player has no more parachute the game is over.
