from core.portfolio_manager import PortfolioManager


class AnalyticsManager:

    def __init__(self):

        self.portfolio = PortfolioManager()


    def get_analytics(self, username):

        stocks = self.portfolio.get_portfolio(
            username
        )

        total_value = 0
        total_quantity = 0

        holdings = []

        for stock in stocks:

            symbol = stock.get(
                "symbol",
                "Unknown"
            )

            quantity = float(
                stock.get(
                    "quantity",
                    0
                )
            )

            price = float(
                stock.get(
                    "price",
                    stock.get(
                        "current_price",
                        0
                    )
                )
            )

            value = quantity * price

            total_value += value
            total_quantity += quantity

            holdings.append({

                "symbol": symbol,
                "quantity": quantity,
                "price": price,
                "value": value
            })


        stock_count = len(
            holdings
        )

        if stock_count > 0:

            best_stock = max(

                holdings,

                key=lambda x: x["value"]

            )["symbol"]

            average_value = (
                total_value/stock_count
            )

        else:

            best_stock = "No stocks"

            average_value = 0


        return {

            "total_value": total_value,

            "stock_count": stock_count,

            "total_quantity": total_quantity,

            "best_stock": best_stock,

            "average_value": average_value,

            "holdings": holdings
        }
