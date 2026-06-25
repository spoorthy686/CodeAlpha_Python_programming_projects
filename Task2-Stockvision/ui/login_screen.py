
import customtkinter as ctk
from tkinter import messagebox

from core.auth import AuthManager


class LoginScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        login_callback,
        register_callback
    ):
        super().__init__(master)

        self.master = master

        self.login_callback = login_callback

        self.register_callback = register_callback

        self.auth = AuthManager()

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

    # ==========================
    # Create UI
    # ==========================

    def create_ui(self):

        title = ctk.CTkLabel(

            self,

            text="📈 StockVision Pro+",

            font=(
                "Arial",
                34,
                "bold"
            )
        )

        title.pack(
            pady=(60,10)
        )

        subtitle = ctk.CTkLabel(

            self,

            text="Smart Portfolio Management",

            font=(
                "Arial",
                18
            )
        )

        subtitle.pack(
            pady=(0,30)
        )

        form = ctk.CTkFrame(
            self,
            corner_radius=20
        )

        form.pack(

            padx=40,

            pady=20,

            ipadx=40,

            ipady=25
        )

        # ==================
        # Username
        # ==================

        username_label = ctk.CTkLabel(

            form,

            text="Username"
        )

        username_label.pack(

            anchor="w",

            padx=20,

            pady=(20,5)
        )

        self.username_entry = ctk.CTkEntry(

            form,

            width=320,

            placeholder_text=
            "Enter username"
        )

        self.username_entry.pack(
            padx=20
        )

        # ==================
        # Password
        # ==================

        password_label = ctk.CTkLabel(

            form,

            text="Password"
        )

        password_label.pack(

            anchor="w",

            padx=20,

            pady=(20,5)
        )

        self.password_entry = ctk.CTkEntry(

            form,

            width=320,

            show="*",

            placeholder_text=
            "Enter password"
        )

        self.password_entry.pack(
            padx=20
        )

        # ==================
        # Show Password
        # ==================

        self.show_password_var = ctk.BooleanVar(
            value=False
        )

        checkbox = ctk.CTkCheckBox(

            form,

            text="Show Password",

            variable=
            self.show_password_var,

            command=
            self.toggle_password
        )

        checkbox.pack(
            pady=15
        )

        # ==================
        # Login Button
        # ==================

        login_button = ctk.CTkButton(

            form,

            text="Login",

            width=250,

            command=self.login
        )

        login_button.pack(
            pady=(10,10)
        )

        # ==================
        # Register Button
        # ==================

        register_button = ctk.CTkButton(

            form,

            text="Create Account",

            width=250,

            fg_color=
            "transparent",

            border_width=2,

            command=
            self.go_to_register
        )

        register_button.pack(
            pady=(0,20)
        )

    # ==========================
    # Password Toggle
    # ==========================

    def toggle_password(self):

        if self.show_password_var.get():

            self.password_entry.configure(
                show=""
            )

        else:

            self.password_entry.configure(
                show="*"
            )

    # ==========================
    # Login User
    # ==========================

    def login(self):

        username = (
            self.username_entry
            .get()
            .strip()
        )

        password = (
            self.password_entry
            .get()
        )

        if not username or not password:

            messagebox.showerror(

                "Error",

                "Fill all fields"
            )

            return

        success, message = (

            self.auth.login_user(

                username,

                password
            )
        )

        if success:

            messagebox.showinfo(

                "Success",

                f"Welcome {username}"
            )

            self.destroy()

            self.login_callback(
                username
            )

        else:

            messagebox.showerror(

                "Login Failed",

                message
            )

    # ==========================
    # Open Register Screen
    # ==========================

    def go_to_register(self):

        self.destroy()

        self.register_callback()

