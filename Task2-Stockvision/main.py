import customtkinter as ctk

from ui.login_screen import LoginScreen
from ui.register_screen import RegisterScreen
from ui.dashboard import DashboardScreen
from ui.portfolio_screen import PortfolioScreen
from ui.analytics_screen import AnalyticsScreen
from ui.simulator_screen import SimulatorScreen
from ui.watchlist_screen import WatchlistScreen
from ui.settings_screen import SettingsScreen


class StockVisionApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ========================
        # Window Settings
        # ========================

        self.title(
            "📈 StockVision Pro+"
        )

        self.geometry(
            "1400x850"
        )

        self.minsize(
            1200,
            750
        )

        ctk.set_appearance_mode(
            "dark"
        )

        ctk.set_default_color_theme(
            "blue"
        )

        self.current_screen = None
        self.current_user = None

        self.show_login()

    # ========================
    # Remove Current Screen
    # ========================

    def clear_screen(self):

        if self.current_screen:

            self.current_screen.destroy()

            self.current_screen = None


    # ========================
    # Login Screen
    # ========================

    def show_login(self):

        self.clear_screen()

        self.current_screen = LoginScreen(

            master=self,

            login_callback=self.login_success,

            register_callback=self.show_register
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Register Screen
    # ========================

    def show_register(self):

        self.clear_screen()

        self.current_screen = RegisterScreen(

            master=self,

            login_callback=self.show_login
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Login Success
    # ========================

    def login_success(
        self,
        username
    ):

        self.current_user = username

        self.show_dashboard()


    # ========================
    # Dashboard
    # ========================

    def show_dashboard(self):

        self.clear_screen()

        self.current_screen = DashboardScreen(

            master=self,

            username=self.current_user,

            logout_callback=self.show_login,

            portfolio_callback=self.show_portfolio,

            analytics_callback=self.show_analytics,

            simulator_callback=self.show_simulator,

            settings_callback=self.show_settings,

            watchlist_callback=self.show_watchlist
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Portfolio
    # ========================

    def show_portfolio(self):

        self.clear_screen()

        self.current_screen = PortfolioScreen(

            master=self,

            username=self.current_user,

            back_callback=self.show_dashboard
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Analytics
    # ========================

    def show_analytics(self):

        self.clear_screen()

        self.current_screen = AnalyticsScreen(

            master=self,

            username=self.current_user,

            back_callback=self.show_dashboard
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Simulator
    # ========================

    def show_simulator(self):

        self.clear_screen()

        self.current_screen = SimulatorScreen(

            master=self,

            username=self.current_user,

            back_callback=self.show_dashboard
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Watchlist
    # ========================

    def show_watchlist(self):

        self.clear_screen()

        self.current_screen = WatchlistScreen(

            master=self,

            username=self.current_user,

            back_callback=self.show_dashboard
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Settings
    # ========================

    def show_settings(self):

        self.clear_screen()

        self.current_screen = SettingsScreen(

            master=self,

            username=self.current_user,

            back_callback=self.show_dashboard,

            logout_callback=self.show_login
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # ========================
    # Close App
    # ========================

    def on_closing(self):

        self.destroy()


# ========================
# Run Application
# ========================

if __name__ == "__main__":

    app = StockVisionApp()

    app.protocol(

        "WM_DELETE_WINDOW",

        app.on_closing
    )

    app.mainloop()
