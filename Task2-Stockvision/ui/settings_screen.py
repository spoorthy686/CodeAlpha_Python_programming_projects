import customtkinter as ctk
from tkinter import messagebox

from core.export_manager import ExportManager


class SettingsScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        username,
        back_callback,
        logout_callback
    ):

        super().__init__(master)

        self.username = username

        self.back_callback = (
            back_callback
        )

        self.logout_callback = (
            logout_callback
        )

        self.export_manager = (
            ExportManager()
        )

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

    # ==========================
    # UI
    # ==========================

    def create_ui(self):

        title = ctk.CTkLabel(

            self,

            text="⚙ Settings",

            font=(
                "Arial",
                30,
                "bold"
            )
        )

        title.pack(
            pady=20
        )

        # =====================
        # Top Buttons
        # =====================

        top_frame = ctk.CTkFrame(
            self
        )

        top_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        back_btn = ctk.CTkButton(

            top_frame,

            text="← Dashboard",

            command=
            self.go_back
        )

        back_btn.pack(
            side="left",
            padx=10
        )

        logout_btn = ctk.CTkButton(

            top_frame,

            text="🚪 Logout",

            fg_color="#DC2626",

            hover_color="#B91C1C",

            command=
            self.logout
        )

        logout_btn.pack(
            side="right",
            padx=10
        )

        # =====================
        # Appearance
        # =====================

        appearance_frame = (
            ctk.CTkFrame(
                self
            )
        )

        appearance_frame.pack(

            fill="x",

            padx=20,

            pady=20
        )

        ctk.CTkLabel(

            appearance_frame,

            text="Appearance Mode",

            font=(
                "Arial",
                18,
                "bold"
            )

        ).pack(
            pady=10
        )

        self.mode_menu = (
            ctk.CTkOptionMenu(

                appearance_frame,

                values=[

                    "Dark",

                    "Light",

                    "System"

                ],

                command=
                self.change_theme
            )
        )

        self.mode_menu.pack(
            pady=10
        )

        # =====================
        # Export
        # =====================

        export_frame = (
            ctk.CTkFrame(
                self
            )
        )

        export_frame.pack(

            fill="x",

            padx=20,

            pady=20
        )

        export_label = (
            ctk.CTkLabel(

                export_frame,

                text="Export Data",

                font=(
                    "Arial",
                    18,
                    "bold"
                )
            )
        )

        export_label.pack(
            pady=10
        )

        export_portfolio = (
            ctk.CTkButton(

                export_frame,

                text=
                "📁 Export Portfolio",

                command=
                self.export_portfolio
            )
        )

        export_portfolio.pack(
            pady=10
        )

        export_analytics = (
            ctk.CTkButton(

                export_frame,

                text=
                "📈 Export Analytics",

                command=
                self.export_analytics
            )
        )

        export_analytics.pack(
            pady=10
        )

    # ==========================
    # Theme
    # ==========================

    def change_theme(
        self,
        mode
    ):

        ctk.set_appearance_mode(
            mode
        )

    # ==========================
    # Export Portfolio
    # ==========================

    def export_portfolio(self):

        path = (

            self.export_manager
            .export_portfolio(

                self.username
            )
        )

        messagebox.showinfo(

            "Export Success",

            f"Saved:\n{path}"
        )

    # ==========================
    # Export Analytics
    # ==========================

    def export_analytics(self):

        path = (

            self.export_manager
            .export_analytics(

                self.username
            )
        )

        messagebox.showinfo(

            "Export Success",

            f"Saved:\n{path}"
        )

    # ==========================
    # Navigation
    # ==========================

    def go_back(self):

        self.destroy()

        self.back_callback()

    def logout(self):

        self.destroy()

        self.logout_callback()
