import matplotlib.pyplot as plt
import os


class ChartManager:

    def __init__(self):

        os.makedirs(
            "assets/charts",
            exist_ok=True
        )


    # --------------------
    # Portfolio Pie Chart
    # --------------------

    def create_portfolio_chart(
        self,
        stocks
    ):

        if len(stocks) == 0:

            return None


        labels=[]
        values=[]


        for stock in stocks:

            labels.append(
                stock["symbol"]
            )

            values.append(

                stock["quantity"] *
                stock["price"]
            )


        plt.figure(
            figsize=(7,5)
        )

        plt.pie(

            values,

            labels=labels,

            autopct="%1.1f%%"
        )

        plt.title(
            "Portfolio Allocation"
        )

        path="assets/charts/portfolio_chart.png"

        plt.savefig(
            path
        )

        plt.close()

        return path


    # --------------------
    # Analytics Bar Chart
    # --------------------

    def create_analytics_chart(
        self,
        stocks
    ):

        if len(stocks)==0:

            return None


        symbols=[]
        values=[]


        for stock in stocks:

            symbols.append(
                stock["symbol"]
            )

            values.append(

                stock["quantity"]*
                stock["price"]
            )


        plt.figure(
            figsize=(8,5)
        )

        plt.bar(
            symbols,
            values
        )

        plt.xlabel(
            "Stocks"
        )

        plt.ylabel(
            "Investment"
        )

        plt.title(
            "Investment Distribution"
        )

        path="assets/charts/analytics_chart.png"

        plt.savefig(
            path
        )

        plt.close()

        return path

