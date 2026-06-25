import customtkinter as ctk
from tkinter import messagebox

from core.auth import AuthManager
from core.stock_manager import StockManager


class WatchlistScreen(ctk.CTkFrame):

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

        self.auth = AuthManager()

        self.stock_manager = (
            StockManager()
        )

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

        self.load_watchlist()


    # ======================
    # UI
    # ======================

    def create_ui(self):

        title = ctk.CTkLabel(

            self,

            text="👁 Watchlist",

            font=(
                "Arial",
                30,
                "bold"
            )
        )

        title.pack(
            pady=20
        )


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

            command=self.go_back
        )

        back_btn.pack(
            side="left",
            padx=10
        )


        refresh_btn = ctk.CTkButton(

            top_frame,

            text="🔄 Refresh",

            command=self.load_watchlist
        )

        refresh_btn.pack(
            side="right",
            padx=10
        )


        # ===================
        # Add Stock
        # ===================

        add_frame = ctk.CTkFrame(
            self
        )

        add_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        self.symbol_entry = (

            ctk.CTkEntry(

                add_frame,

                width=250,

                placeholder_text=
                "Stock Symbol"
            )
        )

        self.symbol_entry.pack(
            side="left",
            padx=10
        )


        add_btn = ctk.CTkButton(

            add_frame,

            text="➕ Add",

            command=self.add_stock
        )

        add_btn.pack(
            side="left",
            padx=10
        )


        # ===================

        self.watchlist_frame = (

            ctk.CTkScrollableFrame(
                self
            )
        )

        self.watchlist_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20
        )


    # ======================
    # Load Watchlist
    # ======================

    def load_watchlist(self):

        for widget in (

            self.watchlist_frame
            .winfo_children()

        ):

            widget.destroy()


        user = (

            self.auth
            .get_user_data(
                self.username
            )
        )


        watchlist = user.get(

            "watchlist",

            []
        )


        # remove duplicates
        watchlist = list(
            set(watchlist)
        )


        if not watchlist:

            empty = ctk.CTkLabel(

                self.watchlist_frame,

                text=
                "No stocks in watchlist",

                font=(
                    "Arial",
                    18
                )
            )

            empty.pack(
                pady=30
            )

            return


        for symbol in watchlist:

            try:

                stock = (

                    self.stock_manager
                    .get_stock_info(
                        symbol
                    )
                )


                row = ctk.CTkFrame(
                    self.watchlist_frame
                )

                row.pack(

                    fill="x",

                    pady=5
                )


                text=(

                    f"{stock.get('symbol','N/A')} | "

                    f"{stock.get('name','Unknown')} | "

                    f"${stock.get('price',0)} | "

                    f"{round(stock.get('change',0),2)}%"
                )


                label = (

                    ctk.CTkLabel(

                        row,

                        text=text
                    )
                )

                label.pack(
                    side="left",
                    padx=10
                )


                remove_btn = (

                    ctk.CTkButton(

                        row,

                        text="🗑 Remove",

                        width=100,

                        fg_color="#DC2626",

                        command=
                        lambda s=symbol:
                        self.remove_stock(
                            s
                        )
                    )
                )

                remove_btn.pack(
                    side="right",
                    padx=10
                )

            except:

                continue


    # ======================
    # Add Stock
    # ======================

    def add_stock(self):

        symbol=(

            self.symbol_entry
            .get()
            .upper()
        )


        if not symbol:

            messagebox.showerror(

                "Error",

                "Enter stock symbol"
            )

            return


        user=(

            self.auth
            .get_user_data(
                self.username
            )
        )


        watchlist=user.get(
            "watchlist",
            []
        )


        if symbol not in watchlist:

            watchlist.append(
                symbol
            )


        user[
            "watchlist"
        ]=watchlist


        self.auth.update_user_data(

            self.username,

            user
        )


        self.symbol_entry.delete(
            0,
            "end"
        )


        self.load_watchlist()


    # ======================
    # Remove Stock
    # ======================

    def remove_stock(
        self,
        symbol
    ):

        user=(

            self.auth
            .get_user_data(
                self.username
            )
        )


        watchlist=user.get(
            "watchlist",
            []
        )


        if symbol in watchlist:

            watchlist.remove(
                symbol
            )


        user[
            "watchlist"
        ]=watchlist


        self.auth.update_user_data(

            self.username,

            user
        )


        self.load_watchlist()


    # ======================
    # Back
    # ======================

    def go_back(self):

        self.destroy()

        self.back_callback()
