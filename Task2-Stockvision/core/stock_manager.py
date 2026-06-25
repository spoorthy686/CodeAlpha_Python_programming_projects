import yfinance as yf


class StockManager:

    def __init__(self):

        self.fallback_prices = {

            "AAPL":180,

            "TSLA":250,

            "GOOGL":140,

            "MSFT":420,

            "AMZN":175,

            "NVDA":850,

            "META":480
        }

    # ==========================
    # Get Current Price
    # ==========================

    def get_stock_price(
        self,
        symbol
    ):

        try:

            stock = yf.Ticker(
                symbol
            )

            data = stock.history(
                period="1d"
            )

            if not data.empty:

                return round(

                    data["Close"][-1],

                    2
                )

        except:

            pass

        return self.fallback_prices.get(

            symbol.upper(),

            0
        )

    # ==========================
    # Get Complete Info
    # ==========================

    def get_stock_info(
        self,
        symbol
    ):

        try:

            stock = yf.Ticker(
                symbol
            )

            info = stock.info

            return {

                "symbol":
                symbol.upper(),

                "name":
                info.get(
                    "shortName",
                    symbol
                ),

                "price":
                info.get(
                    "currentPrice",
                    0
                ),

                "change":
                info.get(
                    "regularMarketChangePercent",
                    0
                )
            }

        except:

            return {

                "symbol":
                symbol.upper(),

                "name":
                symbol,

                "price":
                self.get_stock_price(
                    symbol
                ),

                "change":
                0
            }

    # ==========================
    # Calculate Investment
    # ==========================

    def calculate_total(
        self,
        portfolio
    ):

        total = 0

        for stock in portfolio:

            symbol = stock["symbol"]

            quantity = stock["quantity"]

            price = self.get_stock_price(
                symbol
            )

            total += (

                price * quantity
            )

        return round(
            total,
            2
        )
