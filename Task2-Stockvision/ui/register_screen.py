import customtkinter as ctk
from tkinter import messagebox

from core.auth import AuthManager


class RegisterScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        login_callback
    ):
        super().__init__(master)

        self.master = master

        self.login_callback = login_callback

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

            text="📝 Create Account",

            font=(
                "Arial",
                32,
                "bold"
            )
        )

        title.pack(
            pady=(50,10)
        )

        subtitle = ctk.CTkLabel(

            self,

            text="Join StockVision Pro+",

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

            ipady=20
        )

        # =====================
        # Username
        # =====================

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
            "Choose username"
        )

        self.username_entry.pack(
            padx=20
        )

        # =====================
        # Email
        # =====================

        email_label = ctk.CTkLabel(

            form,

            text="Email"
        )

        email_label.pack(

            anchor="w",

            padx=20,

            pady=(20,5)
        )

        self.email_entry = ctk.CTkEntry(

            form,

            width=320,

            placeholder_text=
            "Enter email"
        )

        self.email_entry.pack(
            padx=20
        )

        # =====================
        # Password
        # =====================

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
            "Create password"
        )

        self.password_entry.pack(
            padx=20
        )

        # =====================
        # Confirm Password
        # =====================

        confirm_label = ctk.CTkLabel(

            form,

            text="Confirm Password"
        )

        confirm_label.pack(

            anchor="w",

            padx=20,

            pady=(20,5)
        )

        self.confirm_entry = ctk.CTkEntry(

            form,

            width=320,

            show="*",

            placeholder_text=
            "Confirm password"
        )

        self.confirm_entry.pack(
            padx=20
        )

        # =====================
        # Show Password
        # =====================

        self.show_password_var = ctk.BooleanVar(
            value=False
        )

        show_password = ctk.CTkCheckBox(

            form,

            text="Show Passwords",

            variable=
            self.show_password_var,

            command=
            self.toggle_password
        )

        show_password.pack(
            pady=15
        )

        # =====================
        # Register Button
        # =====================

        register_button = ctk.CTkButton(

            form,

            text="Create Account",

            width=250,

            command=
            self.register
        )

        register_button.pack(
            pady=(15,10)
        )

        # =====================
        # Back Button
        # =====================

        back_button = ctk.CTkButton(

            form,

            text="Back to Login",

            fg_color=
            "transparent",

            border_width=2,

            command=
            self.go_back
        )

        back_button.pack(
            pady=(0,20)
        )

    # ==========================
    # Toggle Password Visibility
    # ==========================

    def toggle_password(self):

        if self.show_password_var.get():

            self.password_entry.configure(
                show=""
            )

            self.confirm_entry.configure(
                show=""
            )

        else:

            self.password_entry.configure(
                show="*"
            )

            self.confirm_entry.configure(
                show="*"
            )

    # ==========================
    # Register User
    # ==========================

    def register(self):

        username = (
            self.username_entry
            .get()
            .strip()
        )

        email = (
            self.email_entry
            .get()
            .strip()
        )

        password = (
            self.password_entry
            .get()
        )

        confirm_password = (
            self.confirm_entry
            .get()
        )

        if not username or not email or not password:

            messagebox.showerror(

                "Error",

                "Please fill all fields"
            )

            return

        if password != confirm_password:

            messagebox.showerror(

                "Error",

                "Passwords do not match"
            )

            return

        success, message = (

            self.auth.register_user(

                username,

                password,

                email
            )
        )

        if success:

            messagebox.showinfo(

                "Success",

                "Account created successfully!"
            )

            self.destroy()

            self.login_callback()

        else:

            messagebox.showerror(

                "Registration Failed",

                message
            )

    # ==========================
    # Back to Login
    # ==========================

    def go_back(self):

        self.destroy()

        self.login_callback()

