import os
import csv
from datetime import datetime


class ExportManager:

    def __init__(self):

        self.export_folder = os.path.join(
            "data",
            "exports"
        )

        # If exports exists as a file,
        # remove it and create folder

        if os.path.exists(
            self.export_folder
        ):

            if os.path.isfile(
                self.export_folder
            ):

                os.remove(
                    self.export_folder
                )

        os.makedirs(
            self.export_folder,
            exist_ok=True
        )

    # ======================
    # Timestamp
    # ======================

    def get_timestamp(self):

        return datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

    # ======================
    # Export Portfolio
    # ======================

    def export_portfolio(
        self,
        username
    ):

        filename = f"portfolio_{self.get_timestamp()}.csv"

        filepath = os.path.join(
            self.export_folder,
            filename
        )

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow([
                "Username",
                username
            ])

            writer.writerow([
                "Exported",
                datetime.now()
            ])

        return filepath


    # ======================
    # Export Analytics
    # ======================

    def export_analytics(
        self,
        username
    ):

        filename = f"analytics_{self.get_timestamp()}.csv"

        filepath = os.path.join(
            self.export_folder,
            filename
        )

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow([
                "Username",
                username
            ])

            writer.writerow([
                "Exported",
                datetime.now()
            ])

        return filepath

