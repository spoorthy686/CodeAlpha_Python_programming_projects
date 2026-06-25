import customtkinter as ctk
from tkinter import messagebox

from core.portfolio_manager import PortfolioManager


class AddStockScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        username,
        back_callback
    ):

        super().__init__(master)

        self.username = username

        self.back_callback = (
            back_callback
        )

        self.manager = (
            PortfolioManager()
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

            text="➕ Add Stock",

            font=(
                "Arial",
                30,
                "bold"
            )
        )

        title.pack(
            pady=30
        )


        container = ctk.CTkFrame(
            self
        )

        container.pack(
            pady=20,
            padx=20,
            ipadx=30,
            ipady=20
        )


        # -----------------

        symbol_label = ctk.CTkLabel(

            container,

            text="Stock Symbol"
        )

        symbol_label.pack(
            anchor="w",
            padx=10,
            pady=(10,5)
        )


        self.symbol_entry = (
            ctk.CTkEntry(

                container,

                width=300,

                placeholder_text=
                "Example: AAPL"
            )
        )

        self.symbol_entry.pack(
            padx=10,
            pady=5
        )


        # -----------------

        quantity_label = (
            ctk.CTkLabel(

                container,

                text="Quantity"
            )
        )

        quantity_label.pack(
            anchor="w",
            padx=10,
            pady=(15,5)
        )


        self.quantity_entry = (
            ctk.CTkEntry(

                container,

                width=300,

                placeholder_text=
                "Example: 5"
            )
        )

        self.quantity_entry.pack(
            padx=10,
            pady=5
        )


        # -----------------

        add_btn = ctk.CTkButton(

            container,

            text="Add Stock",

            width=250,

            command=self.add_stock
        )

        add_btn.pack(
            pady=20
        )


        # -----------------

        back_btn = ctk.CTkButton(

            container,

            text="← Back",

            fg_color=
            "transparent",

            border_width=2,

            command=
            self.go_back
        )

        back_btn.pack(
            pady=10
        )


    # ==========================
    # Add stock
    # ==========================

    def add_stock(self):

        symbol = (
            self.symbol_entry
            .get()
            .strip()
            .upper()
        )

        quantity = (
            self.quantity_entry
            .get()
        )


        if not symbol:

            messagebox.showerror(

                "Error",

                "Enter stock symbol"
            )

            return


        if not quantity:

            messagebox.showerror(

                "Error",

                "Enter quantity"
            )

            return


        try:

            quantity = int(
                quantity
            )

        except:

            messagebox.showerror(

                "Error",

                "Quantity must be numeric"
            )

            return


        # Allowed stocks

        valid_stocks = [

            "AAPL",
            "TSLA",
            "MSFT",
            "GOOGL",
            "AMZN",
            "NVDA",
            "META"
        ]


        if symbol not in valid_stocks:

            messagebox.showerror(

                "Error",

                "Enter valid stock"
            )

            return


        success, message = (

            self.manager
            .add_stock(

                self.username,

                symbol,

                quantity
            )
        )


        if success:

            messagebox.showinfo(

                "Success",

                "Stock stored successfully"
            )

            self.symbol_entry.delete(
                0,
                "end"
            )

            self.quantity_entry.delete(
                0,
                "end"
            )

        else:

            messagebox.showerror(

                "Error",

                message
            )


    # ==========================
    # Back
    # ==========================

    def go_back(self):

        self.destroy()

        self.back_callback()
