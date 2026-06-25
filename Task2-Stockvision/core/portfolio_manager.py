import json
import os


class PortfolioManager:

    def __init__(self):

        self.file = "data/portfolio.json"

        os.makedirs(
            "data",
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    {},
                    f,
                    indent=4
                )


    # ==========================
    # Load Data
    # ==========================

    def load_data(self):

        try:

            with open(
                self.file,
                "r"
            ) as f:

                return json.load(f)

        except:

            return {}


    # ==========================
    # Save Data
    # ==========================

    def save_data(
        self,
        data
    ):

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )


    # ==========================
    # Add Stock
    # ==========================

    def add_stock(
        self,
        username,
        symbol,
        quantity,
        price
    ):

        data = self.load_data()

        if username not in data:

            data[username] = []


        stock = {

            "symbol": symbol.upper(),

            "quantity": float(quantity),

            "price": float(price)
        }


        data[username].append(
            stock
        )


        self.save_data(
            data
        )


        return True, "Stock added successfully"


    # ==========================
    # Remove Stock
    # ==========================

    def remove_stock(
        self,
        username,
        symbol
    ):

        data = self.load_data()

        if username not in data:

            return False


        stocks = data[username]


        for i, stock in enumerate(stocks):

            if stock["symbol"] == symbol:

                del stocks[i]

                break


        data[username] = stocks


        self.save_data(
            data
        )

        return True


    # ==========================
    # Get Portfolio
    # ==========================

    def get_portfolio(
        self,
        username
    ):

        data = self.load_data()

        return data.get(
            username,
            []
        )


    # ==========================
    # Portfolio Summary
    # ==========================

    def get_portfolio_summary(
        self,
        username
    ):

        stocks = self.get_portfolio(
            username
        )

        total = 0


        for stock in stocks:

            total += (

                stock.get(
                    "quantity",
                    0
                )

                *

                stock.get(
                    "price",
                    0
                )
            )


        return {

            "stocks": stocks,

            "total_value": total,

            "total_stocks": len(stocks)
        }