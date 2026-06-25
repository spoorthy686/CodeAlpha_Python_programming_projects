import customtkinter as ctk
from PIL import Image
from core.portfolio_manager import PortfolioManager


class DashboardScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        username,
        logout_callback,
        portfolio_callback,
        analytics_callback,
        simulator_callback,
        settings_callback,
        watchlist_callback
    ):

        super().__init__(master)

        self.username = username

        self.logout_callback = logout_callback
        self.portfolio_callback = portfolio_callback
        self.analytics_callback = analytics_callback
        self.simulator_callback = simulator_callback
        self.settings_callback = settings_callback
        self.watchlist_callback = watchlist_callback

        self.portfolio = PortfolioManager()

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()


    # =====================
    # Portfolio Statistics
    # =====================

    def get_stats(self):

        stocks = self.portfolio.get_portfolio(
            self.username
        )

        total = 0

        for stock in stocks:

            quantity = stock.get(
                "quantity",
                0
            )

            price = stock.get(
                "price",
                stock.get(
                    "current_price",
                    0
                )
            )

            total += quantity * price

        return total, len(stocks)


    # =====================
    # Dashboard UI
    # =====================

    def create_ui(self):

        # ================= Sidebar =================

        sidebar = ctk.CTkFrame(
            self,
            width=220
        )

        sidebar.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )


        # Logo

        logo = ctk.CTkImage(
            Image.open(
                "assets/logo.png"
            ),
            size=(100,100)
        )

        logo_label = ctk.CTkLabel(
            sidebar,
            image=logo,
            text=""
        )

        logo_label.image = logo

        logo_label.pack(
            pady=15
        )


        title = ctk.CTkLabel(

            sidebar,

            text="StockVision",

            font=(
                "Arial",
                22,
                "bold"
            )
        )

        title.pack(
            pady=10
        )


        # Sidebar Buttons

        buttons=[

            (
                "📁 Portfolio",
                self.portfolio_callback
            ),

            (
                "📊 Analytics",
                self.analytics_callback
            ),

            (
                "🧮 Simulator",
                self.simulator_callback
            ),

            (
                "👁 Watchlist",
                self.watchlist_callback
            ),

            (
                "⚙ Settings",
                self.settings_callback
            )
        ]


        for text,command in buttons:

            btn=ctk.CTkButton(

                sidebar,

                text=text,

                command=command,

                width=160,

                height=40
            )

            btn.pack(

                pady=10,

                padx=10
            )


        logout_btn=ctk.CTkButton(

            sidebar,

            text="🚪 Logout",

            fg_color="red",

            command=self.logout_callback
        )

        logout_btn.pack(

            side="bottom",

            pady=20,

            padx=10
        )


        # ================= Main Content =================

        content=ctk.CTkFrame(
            self
        )

        content.pack(

            side="left",

            fill="both",

            expand=True,

            padx=10,

            pady=10
        )


        # Banner

        banner=ctk.CTkImage(

            Image.open(
                "assets/images/dashboard_banner.png"
            ),

            size=(1000,250)
        )


        banner_label=ctk.CTkLabel(

            content,

            image=banner,

            text=""
        )

        banner_label.image=banner

        banner_label.pack(
            pady=10
        )


        # Welcome

        welcome=ctk.CTkLabel(

            content,

            text=f"Welcome, {self.username}",

            font=(

                "Arial",

                32,

                "bold"
            )
        )

        welcome.pack(
            pady=20
        )


        # Statistics

        total,count=self.get_stats()


        stats_frame=ctk.CTkFrame(
            content
        )

        stats_frame.pack(
            pady=25
        )


        value_card=ctk.CTkFrame(

            stats_frame,

            width=300,

            height=120
        )

        value_card.grid(
            row=0,
            column=0,
            padx=30
        )


        value=ctk.CTkLabel(

            value_card,

            text=f"Portfolio Value\n${total:.2f}",

            font=(
                "Arial",
                18,
                "bold"
            )
        )

        value.pack(
            pady=30
        )


        stock_card=ctk.CTkFrame(

            stats_frame,

            width=300,

            height=120
        )

        stock_card.grid(

            row=0,

            column=1,

            padx=30
        )


        stock=ctk.CTkLabel(

            stock_card,

            text=f"Stocks Owned\n{count}",

            font=(

                "Arial",

                18,

                "bold"
            )
        )

        stock.pack(
            pady=30
        )
