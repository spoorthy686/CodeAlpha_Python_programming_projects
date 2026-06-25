import customtkinter as ctk
from tkinter import messagebox

from core.portfolio_manager import PortfolioManager


class PortfolioScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        username,
        back_callback
    ):

        super().__init__(master)

        self.username = username
        self.back_callback = back_callback

        self.manager = PortfolioManager()

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

        self.load_portfolio()


    # =========================
    # UI
    # =========================

    def create_ui(self):

        title = ctk.CTkLabel(

            self,

            text="📁 Portfolio Manager",

            font=("Arial",30,"bold")
        )

        title.pack(
            pady=20
        )


        input_frame = ctk.CTkFrame(
            self
        )

        input_frame.pack(
            pady=15
        )


        self.symbol_entry = ctk.CTkEntry(

            input_frame,

            placeholder_text="Stock Symbol (AAPL)",

            width=200
        )

        self.symbol_entry.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )


        self.quantity_entry = ctk.CTkEntry(

            input_frame,

            placeholder_text="Quantity",

            width=150
        )

        self.quantity_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )


        self.price_entry = ctk.CTkEntry(

            input_frame,

            placeholder_text="Price",

            width=150
        )

        self.price_entry.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )


        add_button = ctk.CTkButton(

            input_frame,

            text="Add Stock",

            command=self.add_stock
        )

        add_button.grid(
            row=0,
            column=3,
            padx=10
        )


        self.summary_label = ctk.CTkLabel(

            self,

            text="",

            font=("Arial",18,"bold")
        )

        self.summary_label.pack(
            pady=15
        )


        self.portfolio_frame = (

            ctk.CTkScrollableFrame(

                self,

                width=900,

                height=350
            )
        )

        self.portfolio_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=15
        )


        back_button = ctk.CTkButton(

            self,

            text="← Back to Dashboard",

            command=self.back_callback
        )

        back_button.pack(
            pady=20
        )


    # =========================
    # Add Stock
    # =========================

    def add_stock(self):

        symbol = self.symbol_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if (

            symbol == ""
            or quantity == ""
            or price == ""

        ):

            messagebox.showerror(

                "Error",

                "Fill all fields"
            )

            return


        try:

            quantity = float(quantity)
            price = float(price)

        except:

            messagebox.showerror(

                "Error",

                "Quantity and Price must be numbers"
            )

            return


        self.manager.add_stock(

            self.username,

            symbol,

            quantity,

            price
        )


        self.load_portfolio()


        self.symbol_entry.delete(
            0,
            "end"
        )

        self.quantity_entry.delete(
            0,
            "end"
        )

        self.price_entry.delete(
            0,
            "end"
        )


    # =========================
    # Remove Stock
    # =========================

    def remove_stock(
        self,
        symbol
    ):

        confirm = messagebox.askyesno(

            "Confirm",

            f"Remove {symbol}?"
        )

        if not confirm:

            return


        self.manager.remove_stock(

            self.username,

            symbol
        )

        self.load_portfolio()


    # =========================
    # Load Portfolio
    # =========================

    def load_portfolio(self):

        summary = self.manager.get_portfolio_summary(
            self.username
        )

        stocks = summary["stocks"]


        self.summary_label.configure(

            text=

            f"📦 Total Stocks: {summary['total_stocks']}     "

            f"💰 Portfolio Value: ${summary['total_value']:.2f}"
        )


        for widget in (
            self.portfolio_frame.winfo_children()
        ):

            widget.destroy()


        if len(stocks) == 0:

            empty = ctk.CTkLabel(

                self.portfolio_frame,

                text="No stocks added.",

                font=("Arial",20)
            )

            empty.pack(
                pady=50
            )

            return


        cards_per_row = 3


        for i, stock in enumerate(stocks):

            card = ctk.CTkFrame(

                self.portfolio_frame,

                width=250,

                height=200
            )

            row = i // cards_per_row
            col = i % cards_per_row

            card.grid(

                row=row,

                column=col,

                padx=20,

                pady=20
            )


            ctk.CTkLabel(

                card,

                text=stock["symbol"],

                font=("Arial",20,"bold")

            ).pack(
                pady=(10,5)
            )


            ctk.CTkLabel(

                card,

                text=f"Quantity : {stock['quantity']}"

            ).pack()


            ctk.CTkLabel(

                card,

                text=f"Price : ${stock['price']}"

            ).pack()


            total = (

                stock["quantity"]
                *
                stock["price"]
            )


            ctk.CTkLabel(

                card,

                text=f"Value : ${total:.2f}",

                font=("Arial",14,"bold")

            ).pack(
                pady=5
            )


            remove_btn = ctk.CTkButton(

                card,

                text="🗑 Remove",

                width=120,

                fg_color="#DC2626",

                command=lambda s=stock["symbol"]:
                self.remove_stock(s)
            )

            remove_btn.pack(
                pady=10
            )

