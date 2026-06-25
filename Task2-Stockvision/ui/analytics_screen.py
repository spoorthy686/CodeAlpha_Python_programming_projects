import customtkinter as ctk
from core.analytics import AnalyticsManager


class AnalyticsScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        username,
        back_callback
    ):

        super().__init__(master)

        self.username = username
        self.back_callback = back_callback

        self.analytics = AnalyticsManager()

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

        self.load_analytics()


    # ======================
    # UI
    # ======================

    def create_ui(self):

        title = ctk.CTkLabel(

            self,

            text="📊 Analytics Dashboard",

            font=(
                "Arial",
                32,
                "bold"
            )
        )

        title.pack(
            pady=20
        )


        # Main Container

        self.main_frame = ctk.CTkFrame(
            self
        )

        self.main_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10
        )


        # ===================
        # Summary Cards
        # ===================

        self.card_frame = ctk.CTkFrame(
            self.main_frame
        )

        self.card_frame.pack(

            fill="x",

            pady=20
        )


        # ===================
        # Holdings Title
        # ===================

        holdings_title = ctk.CTkLabel(

            self.main_frame,

            text="📦 Stock Holdings",

            font=(
                "Arial",
                22,
                "bold"
            )
        )

        holdings_title.pack(
            pady=10
        )


        # ===================
        # Holdings Area
        # ===================

        self.holdings_frame = (

            ctk.CTkScrollableFrame(

                self.main_frame,

                height=300
            )
        )

        self.holdings_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10
        )


        # ===================
        # Back Button
        # ===================

        back_btn = ctk.CTkButton(

            self,

            text="← Dashboard",

            width=150,

            command=self.back_callback
        )

        back_btn.pack(
            pady=20
        )


    # ======================
    # Card Widget
    # ======================

    def create_card(

        self,

        parent,

        title,

        value,

        column
    ):

        card = ctk.CTkFrame(

            parent,

            width=220,

            height=100
        )

        card.grid(

            row=0,

            column=column,

            padx=15,

            pady=10
        )


        title_label = ctk.CTkLabel(

            card,

            text=title,

            font=(
                "Arial",
                16
            )
        )

        title_label.pack(
            pady=(15,5)
        )


        value_label = ctk.CTkLabel(

            card,

            text=str(value),

            font=(
                "Arial",
                22,
                "bold"
            )
        )

        value_label.pack(
            pady=5
        )


    # ======================
    # Load Analytics
    # ======================

    def load_analytics(self):

        data = self.analytics.get_analytics(
            self.username
        )


        # Clear previous cards

        for widget in (
            self.card_frame.winfo_children()
        ):
            widget.destroy()


        self.create_card(

            self.card_frame,

            "💰 Portfolio",

            f"${round(data['total_value'],2)}",

            0
        )


        self.create_card(

            self.card_frame,

            "📦 Stocks",

            data["stock_count"],

            1
        )


        self.create_card(

            self.card_frame,

            "⭐ Best",

            data["best_stock"],

            2
        )


        self.create_card(

            self.card_frame,

            "📈 Average",

            f"${round(data['average_value'],2)}",

            3
        )


        # ===================
        # Clear old holdings
        # ===================

        for widget in (
            self.holdings_frame.winfo_children()
        ):
            widget.destroy()


        # ===================
        # Create stock cards
        # ===================

        for i,stock in enumerate(

            data["holdings"]

        ):

            stock_card = ctk.CTkFrame(

                self.holdings_frame,

                width=250,

                height=150
            )

            stock_card.grid(

                row=i//3,

                column=i%3,

                padx=15,

                pady=15
            )


            symbol = ctk.CTkLabel(

                stock_card,

                text=stock["symbol"],

                font=(
                    "Arial",
                    20,
                    "bold"
                )
            )

            symbol.pack(
                pady=(10,5)
            )


            quantity = ctk.CTkLabel(

                stock_card,

                text=f"Qty : {stock['quantity']}"
            )

            quantity.pack()


            price = ctk.CTkLabel(

                stock_card,

                text=f"Price : ${stock['price']}"
            )

            price.pack()


            value = ctk.CTkLabel(

                stock_card,

                text=f"Value : ${round(stock['value'],2)}",

                font=(
                    "Arial",
                    14,
                    "bold"
                )
            )

            value.pack(
                pady=10
            )