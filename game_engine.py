import random


class HangmanGame:

    def __init__(
        self,
        word,
        category,
        difficulty
    ):

        self.word = word.upper()

        self.category = category
        self.difficulty = difficulty

        self.guessed_letters = set()

        self.max_lives = 6
        self.lives = self.max_lives

        self.score = 0
        self.coins = 50

        self.game_over = False
        self.won = False

    # ==========================
    # DISPLAY WORD
    # ==========================

    def get_display_word(self):

        display = []

        for letter in self.word:

            if letter in self.guessed_letters:
                display.append(letter)

            else:
                display.append("_")

        return " ".join(display)

    # ==========================
    # GUESS LETTER
    # ==========================

    def guess_letter(self, letter):

        letter = letter.upper()

        if self.game_over:

            return {
                "status": "finished",
                "message": "Game already finished."
            }

        if letter in self.guessed_letters:

            return {
                "status": "already",
                "message": f"{letter} already guessed."
            }

        self.guessed_letters.add(letter)

        # Correct Guess
        if letter in self.word:

            self.score += 10

            if self.check_win():

                self.game_over = True
                self.won = True

                self.score += 50

                return {
                    "status": "win",
                    "message": "You won!"
                }

            return {
                "status": "correct",
                "message": f"{letter} is correct."
            }

        # Wrong Guess
        self.lives -= 1

        if self.lives <= 0:

            self.game_over = True

            return {
                "status": "lose",
                "message": "Game Over."
            }

        return {
            "status": "wrong",
            "message": f"{letter} is incorrect."
        }

    # ==========================
    # CHECK WIN
    # ==========================

    def check_win(self):

        for letter in self.word:

            if letter not in self.guessed_letters:

                return False

        return True

    # ==========================
    # USE HINT
    # ==========================

    def use_hint(self):

        HINT_COST = 20

        if self.coins < HINT_COST:

            return {
                "success": False,
                "message": "Not enough coins."
            }

        hidden_letters = []

        for letter in self.word:

            if letter not in self.guessed_letters:

                hidden_letters.append(letter)

        if not hidden_letters:

            return {
                "success": False,
                "message": "No hints available."
            }

        revealed = random.choice(hidden_letters)

        self.guessed_letters.add(revealed)

        self.coins -= HINT_COST

        self.score += 5

        # Check if hint caused victory
        if self.check_win():

            self.game_over = True
            self.won = True

            self.score += 50

        return {
            "success": True,
            "letter": revealed,
            "message": f"Revealed {revealed}"
        }

    # ==========================
    # GAME STATS
    # ==========================

    def get_stats(self):

        return {

            "word": self.word,

            "category": self.category,

            "difficulty": self.difficulty,

            "score": self.score,

            "coins": self.coins,

            "lives": self.lives,

            "guessed": sorted(
                list(self.guessed_letters)
            ),

            "game_over": self.game_over,

            "won": self.won
        }