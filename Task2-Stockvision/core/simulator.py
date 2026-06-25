from core.stock_manager import StockManager


class Simulator:

    def __init__(self):

        self.stock_manager = (
            StockManager()
        )

    # ==========================
    # Simulate Investment
    # ==========================

    def simulate_investment(
        self,
        symbol,
        amount,
        years,
        annual_growth=10
    ):

        symbol = symbol.upper()

        current_price = (

            self.stock_manager
            .get_stock_price(
                symbol
            )
        )

        if current_price <= 0:

            return {

                "success": False,

                "message":
                "Invalid stock symbol"
            }

        shares = (

            amount /
            current_price
        )

        results = []

        current_value = amount

        for year in range(
            years + 1
        ):

            if year > 0:

                current_value *= (

                    1 +
                    (
                        annual_growth /
                        100
                    )
                )

            profit = (

                current_value -
                amount
            )

            results.append({

                "year":
                year,

                "value":
                round(
                    current_value,
                    2
                ),

                "profit":
                round(
                    profit,
                    2
                )
            })

        return {

            "success": True,

            "symbol":
            symbol,

            "current_price":
            current_price,

            "shares":
            round(
                shares,
                2
            ),

            "initial_amount":
            amount,

            "growth_rate":
            annual_growth,

            "years":
            years,

            "results":
            results
        }

    # ==========================
    # Chart Data
    # ==========================

    def get_chart_data(
        self,
        simulation
    ):

        years = []

        values = []

        for item in (
            simulation[
                "results"
            ]
        ):

            years.append(
                item["year"]
            )

            values.append(
                item["value"]
            )

        return {

            "years":
            years,

            "values":
            values
        }

