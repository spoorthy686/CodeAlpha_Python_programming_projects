import customtkinter as ctk


class SimulatorScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        username,
        back_callback
    ):

        super().__init__(master)

        self.username = username
        self.back_callback = back_callback

        self.pack(
            fill="both",
            expand=True
        )

        self.create_ui()


    def create_ui(self):

        title = ctk.CTkLabel(

            self,

            text="📈 Investment Simulator",

            font=("Arial",30,"bold")
        )

        title.pack(
            pady=20
        )


        back_btn = ctk.CTkButton(

            self,

            text="← Dashboard",

            command=self.back_callback
        )

        back_btn.pack(
            pady=10
        )


        self.symbol_entry = ctk.CTkEntry(

            self,

            width=300,

            placeholder_text="Stock Symbol"
        )

        self.symbol_entry.pack(
            pady=10
        )


        self.amount_entry = ctk.CTkEntry(

            self,

            width=300,

            placeholder_text="Investment Amount"
        )

        self.amount_entry.pack(
            pady=10
        )


        self.years_entry = ctk.CTkEntry(

            self,

            width=300,

            placeholder_text="Years"
        )

        self.years_entry.pack(
            pady=10
        )


        self.growth_entry = ctk.CTkEntry(

            self,

            width=300,

            placeholder_text="Growth Rate (%)"
        )

        self.growth_entry.pack(
            pady=10
        )


        simulate_btn = ctk.CTkButton(

            self,

            text="📊 Start Investment",

            command=self.run_simulation
        )

        simulate_btn.pack(
            pady=20
        )


        # Results section

        result_title = ctk.CTkLabel(

            self,

            text="📈 Simulation Results",

            font=(
                "Arial",
                22,
                "bold"
            )
        )

        result_title.pack(
            pady=10
        )


        self.result_frame = (

            ctk.CTkScrollableFrame(

                self,

                height=350
            )
        )

        self.result_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20
        )


    def run_simulation(self):

        try:

            amount = float(
                self.amount_entry.get()
            )

            years = int(
                self.years_entry.get()
            )

            growth = float(
                self.growth_entry.get()
            )

        except:

            return


        # Clear previous results

        for widget in (
            self.result_frame.winfo_children()
        ):

            widget.destroy()


        value = amount

        cards_per_row = 3


        # Center columns

        for col in range(cards_per_row):

            self.result_frame.grid_columnconfigure(

                col,

                weight=1
            )


        for year in range(years+1):

            row = year // cards_per_row

            col = year % cards_per_row


            card = ctk.CTkFrame(

                self.result_frame,

                width=220,

                height=140
            )

            card.grid_propagate(
                False
            )


            card.grid(

                row=row,

                column=col,

                padx=20,

                pady=20,

                sticky=""
            )


            year_label = ctk.CTkLabel(

                card,

                text=f"Year {year}",

                font=(

                    "Arial",

                    18,

                    "bold"
                )
            )

            year_label.pack(
                pady=(15,5)
            )


            amount_label = ctk.CTkLabel(

                card,

                text=f"${value:.2f}",

                font=(

                    "Arial",

                    22,

                    "bold"
                )
            )

            amount_label.pack(
                pady=5
            )


            growth_label = ctk.CTkLabel(

                card,

                text=f"Growth: {growth}%"
            )

            growth_label.pack(
                pady=5
            )


            value *= (

                1 + growth/100
            )
