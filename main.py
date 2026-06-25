import customtkinter as ctk
from tkinter import messagebox

from game.word_bank import (
    get_categories,
    get_difficulties
)

from ui.game_screen import GameScreen


# ==================================
# MAIN APPLICATION
# ==================================

class HangmanApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("🎮 Hangman Deluxe")

        self.geometry("1000x900")

        self.resizable(False, False)

        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")

        self.current_screen = None

        self.show_dashboard()

    # ==================================
    # CLEAR SCREEN
    # ==================================

    def clear_screen(self):

        for widget in self.winfo_children():

            widget.destroy()

    # ==================================
    # DASHBOARD
    # ==================================

    def show_dashboard(self):

        self.clear_screen()

        dashboard = ctk.CTkFrame(self)

        dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # -------------------------
        # Title
        # -------------------------

        title = ctk.CTkLabel(
            dashboard,
            text="🎮 Hangman Deluxe",
            font=("Arial", 36, "bold")
        )

        title.pack(
            pady=(30, 10)
        )

        subtitle = ctk.CTkLabel(
            dashboard,
            text="Choose your category and difficulty",
            font=("Arial", 18)
        )

        subtitle.pack(
            pady=(0, 30)
        )

        # -------------------------
        # Category Selection
        # -------------------------

        category_label = ctk.CTkLabel(
            dashboard,
            text="Category",
            font=("Arial", 18, "bold")
        )

        category_label.pack(
            pady=(10, 5)
        )

        self.category_var = ctk.StringVar(
            value=get_categories()[0]
        )

        self.category_menu = ctk.CTkOptionMenu(
            dashboard,
            values=get_categories(),
            variable=self.category_var,
            width=250
        )

        self.category_menu.pack(
            pady=10
        )

        # -------------------------
        # Difficulty Selection
        # -------------------------

        difficulty_label = ctk.CTkLabel(
            dashboard,
            text="Difficulty",
            font=("Arial", 18, "bold")
        )

        difficulty_label.pack(
            pady=(20, 5)
        )

        self.difficulty_var = ctk.StringVar(
            value="Easy"
        )

        self.difficulty_menu = ctk.CTkOptionMenu(
            dashboard,
            values=get_difficulties(),
            variable=self.difficulty_var,
            width=250
        )

        self.difficulty_menu.pack(
            pady=10
        )

        # -------------------------
        # Buttons
        # -------------------------

        play_button = ctk.CTkButton(
            dashboard,
            text="▶ Start Game",
            width=250,
            height=50,
            font=("Arial", 18, "bold"),
            command=self.start_game
        )

        play_button.pack(
            pady=(40, 15)
        )

        exit_button = ctk.CTkButton(
            dashboard,
            text="🚪 Exit",
            width=250,
            height=50,
            fg_color="red",
            hover_color="darkred",
            command=self.quit
        )

        exit_button.pack(
            pady=10
        )

    # ==================================
    # START GAME
    # ==================================

    def start_game(self):

        category = self.category_var.get()

        difficulty = self.difficulty_var.get()

        self.clear_screen()

        self.current_screen = GameScreen(
            master=self,
            category=category,
            difficulty=difficulty,
            go_home_callback=self.show_dashboard
        )

    # ==================================
    # CLOSE APP
    # ==================================

    def on_closing(self):

        answer = messagebox.askyesno(
            "Exit",
            "Are you sure you want to quit?"
        )

        if answer:

            self.destroy()


# ==================================
# RUN APPLICATION
# ==================================

if __name__ == "__main__":

    app = HangmanApp()

    app.protocol(
        "WM_DELETE_WINDOW",
        app.on_closing
    )

    app.mainloop()