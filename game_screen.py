# ui/game_screen.py

import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from game.game_engine import HangmanGame
from game.word_bank import get_random_word


CATEGORY_ICONS = {
    "Programming": "🐍",
    "Countries": "🌍",
    "Animals": "🐾",
    "Movies": "🎬",
    "Sports": "⚽"
}


class GameScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        category,
        difficulty,
        go_home_callback
    ):
        super().__init__(master)

        self.master = master
        self.go_home_callback = go_home_callback

        # -------------------------
        # Create Game Instance
        # -------------------------

        word = get_random_word(
            category,
            difficulty
        )

        self.game = HangmanGame(
            word=word,
            category=category,
            difficulty=difficulty
        )

        # -------------------------
        # Load Hangman Images
        # -------------------------

        self.hangman_images = []

        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        for i in range(7):

            image_path = os.path.join(
                BASE_DIR,
                "assets",
                "images",
                f"hangman{i}.png"
            )

            image = ctk.CTkImage(
                light_image=Image.open(
                    image_path
                ),
                dark_image=Image.open(
                    image_path
                ),
                size=(180, 180)
            )

            self.hangman_images.append(
                image
            )

        # -------------------------
        # Layout
        # -------------------------

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # -------------------------
        # Header
        # -------------------------

        self.create_header()

        # -------------------------
        # Hangman Display
        # -------------------------

        self.create_hangman_display()

        # -------------------------
        # Word Display
        # -------------------------

        self.create_word_display()

        # -------------------------
        # Controls
        # -------------------------

        self.create_controls()

        # -------------------------
        # Keyboard
        # -------------------------

        self.create_keyboard()

        # -------------------------
        # Initial Update
        # -------------------------

        self.update_ui()

    # ==================================
    # HEADER
    # ==================================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        header.pack(
            fill="x",
            pady=(0, 15)
        )

        self.category_label = ctk.CTkLabel(
            header,
            text="",
            font=("Arial", 20, "bold")
        )

        self.category_label.pack(
            side="left",
            padx=20,
            pady=15
        )

        self.score_label = ctk.CTkLabel(
            header,
            text="",
            font=("Arial", 18, "bold")
        )

        self.score_label.pack(
            side="right",
            padx=20
        )

    # ==================================
    # HANGMAN IMAGE
    # ==================================

    def create_hangman_display(self):

        self.image_label = ctk.CTkLabel(
            self,
            text="",
            image=self.hangman_images[0]
        )

        self.image_label.pack(
            pady=10
        )

    # ==================================
    # WORD DISPLAY
    # ==================================

    def create_word_display(self):

        word_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        word_frame.pack(
            fill="x",
            pady=10
        )

        self.word_label = ctk.CTkLabel(
            word_frame,
            text="",
            font=("Courier", 32, "bold")
        )

        self.word_label.pack(
            pady=25
        )

    # ==================================
    # CONTROLS
    # ==================================

    def create_controls(self):

        control_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        control_frame.pack(
            fill="x",
            pady=10
        )

        self.lives_label = ctk.CTkLabel(
            control_frame,
            text="",
            font=("Arial", 18, "bold")
        )

        self.lives_label.pack(
            side="left",
            padx=20,
            pady=15
        )

        self.progress_bar = ctk.CTkProgressBar(
            control_frame,
            width=200
        )

        self.progress_bar.pack(
            side="left",
            padx=10
        )

        self.progress_bar.set(1)

        self.hint_button = ctk.CTkButton(
            control_frame,
            text="💡 Hint",
            command=self.use_hint
        )

        self.hint_button.pack(
            side="right",
            padx=10
        )

        self.home_button = ctk.CTkButton(
            control_frame,
            text="🏠 Dashboard",
            command=self.return_home
        )

        self.home_button.pack(
            side="right",
            padx=10
        )

    # ==================================
    # KEYBOARD
    # ==================================

    def create_keyboard(self):

        keyboard_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        keyboard_frame.pack(
            pady=20
        )

        self.letter_buttons = {}

        keyboard_rows = [
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM"
        ]

        for row_letters in keyboard_rows:

            row_frame = ctk.CTkFrame(
                keyboard_frame,
                fg_color="transparent"
            )

            row_frame.pack(
                pady=5
            )

            for letter in row_letters:

                btn = ctk.CTkButton(
                    row_frame,
                    text=letter,
                    width=50,
                    height=50,
                    command=lambda l=letter:
                        self.make_guess(l)
                )

                btn.pack(
                    side="left",
                    padx=4
                )

                self.letter_buttons[
                    letter
                ] = btn
                    # ==================================
    # UPDATE UI
    # ==================================

    def update_ui(self):

        stats = self.game.get_stats()

        # Category Label
        icon = CATEGORY_ICONS.get(
            stats["category"],
            "🎮"
        )

        self.category_label.configure(
            text=(
                f"{icon} "
                f"{stats['category']} | "
                f"{stats['difficulty']}"
            )
        )

        # Score + Coins
        self.score_label.configure(
            text=(
                f"⭐ {stats['score']}   "
                f"🪙 {stats['coins']}"
            )
        )

        # Word Display
        self.word_label.configure(
            text=self.game.get_display_word()
        )

        # Lives
        self.lives_label.configure(
            text=(
                f"❤️ "
                f"{stats['lives']}/"
                f"{self.game.max_lives}"
            )
        )

        # Progress Bar
        self.progress_bar.set(
            stats["lives"] /
            self.game.max_lives
        )

        # Hangman Image
        wrong_guesses = (
            self.game.max_lives -
            stats["lives"]
        )

        wrong_guesses = max(
            0,
            min(wrong_guesses, 6)
        )

        self.image_label.configure(
            image=self.hangman_images[
                wrong_guesses
            ]
        )

        # Hint Button
        if (
            stats["coins"] < 20 or
            stats["game_over"]
        ):

            self.hint_button.configure(
                state="disabled"
            )

        else:

            self.hint_button.configure(
                state="normal"
            )

    # ==================================
    # GUESS HANDLING
    # ==================================

    def make_guess(self, letter):

        self.letter_buttons[
            letter
        ].configure(
            state="disabled"
        )

        result = self.game.guess_letter(
            letter
        )

        self.update_ui()

        status = result["status"]

        if status == "correct":

            messagebox.showinfo(
                "Correct!",
                result["message"]
            )

        elif status == "wrong":

            messagebox.showwarning(
                "Wrong Guess",
                result["message"]
            )

        elif status == "already":

            messagebox.showinfo(
                "Already Guessed",
                result["message"]
            )

        elif status == "win":

            self.show_win_screen()

        elif status == "lose":

            self.show_lose_screen()

    # ==================================
    # HINT SYSTEM
    # ==================================

    def use_hint(self):

        hint = self.game.use_hint()

        if not hint["success"]:

            messagebox.showwarning(
                "Hint",
                hint["message"]
            )

            return

        letter = hint["letter"]

        if letter in self.letter_buttons:

            self.letter_buttons[
                letter
            ].configure(
                state="disabled"
            )

        self.update_ui()

        messagebox.showinfo(
            "Hint Used",
            (
                f"Revealed Letter: "
                f"{letter}\n\n"
                f"Coins Remaining: "
                f"{self.game.coins}"
            )
        )

        if (
            self.game.game_over and
            self.game.won
        ):

            self.show_win_screen()

    # ==================================
    # WIN SCREEN
    # ==================================

    def show_win_screen(self):

        stats = self.game.get_stats()

        self.disable_keyboard()

        answer = messagebox.askyesno(
            "🎉 Victory!",
            (
                f"You guessed the word!\n\n"
                f"Word: {stats['word']}\n"
                f"Score: {stats['score']}\n"
                f"Coins: {stats['coins']}\n"
                f"Lives Left: {stats['lives']}\n\n"
                f"Return to Dashboard?"
            )
        )

        if answer:

            self.return_home()

    # ==================================
    # LOSE SCREEN
    # ==================================

    def show_lose_screen(self):

        stats = self.game.get_stats()

        self.disable_keyboard()

        answer = messagebox.askyesno(
            "💀 Game Over",
            (
                f"The word was:\n"
                f"{stats['word']}\n\n"
                f"Score: {stats['score']}\n"
                f"Coins: {stats['coins']}\n\n"
                f"Return to Dashboard?"
            )
        )

        if answer:

            self.return_home()

    # ==================================
    # DISABLE KEYBOARD
    # ==================================

    def disable_keyboard(self):

        for button in self.letter_buttons.values():

            button.configure(
                state="disabled"
            )

    # ==================================
    # RETURN HOME
    # ==================================

    def return_home(self):

        self.destroy()

        self.go_home_callback()