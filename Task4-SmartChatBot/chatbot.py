from datetime import datetime
import random


class ChatBotEngine:

    def __init__(self):

        self.greetings = [
            "Hello 👋",
            "Hi there 😊",
            "Welcome back 🚀",
            "Nice to see you!"
        ]

    # ======================================
    # HELP MENU
    # ======================================

    def help_menu(self):

        return """
════════════ COMMANDS ════════════

GENERAL
---------------------------------
hello
hi
how are you
time
date
quote
help
bye

NOTES
---------------------------------
add note <text>
show notes
delete note <number>

TASKS
---------------------------------
add task <text>
show tasks
complete task <number>
delete task <number>

GOALS
---------------------------------
add goal <text>
show goals
complete goal <number>
delete goal <number>

UTILITIES
---------------------------------
calculate 25+10
stats
export report

══════════════════════════════════
"""

    # ======================================
    # CALCULATOR
    # ======================================

    def calculate(self, expression):

        allowed = "0123456789+-*/(). "

        for char in expression:

            if char not in allowed:
                return "❌ Invalid Expression"

        try:
            return f"🧮 Result: {eval(expression)}"

        except:
            return "❌ Calculation Error"

    # ======================================
    # RANDOM QUOTES
    # ======================================

    def get_quote(self):

        quotes = [

            "Success is built one step at a time.",

            "Consistency beats motivation.",

            "Small progress is still progress.",

            "Focus on improvement, not perfection.",

            "Discipline creates freedom.",

            "Your future is created by what you do today."

        ]

        return random.choice(quotes)

    # ======================================
    # CHATBOT ENGINE
    # ======================================

    def get_response(
        self,
        user_input,
        notes_manager=None,
        tasks_manager=None,
        goals_manager=None,
        stats_callback=None,
        export_callback=None
    ):

        command = user_input.strip()

        lower = command.lower()

        # ==================================
        # BASIC COMMANDS
        # ==================================

        if lower in ["hello", "hi"]:

            return random.choice(
                self.greetings
            )

        elif lower == "how are you":

            return (
                "I'm doing great and ready to help 😊"
            )

        elif lower == "time":

            return (
                "🕒 " +
                datetime.now().strftime(
                    "%I:%M:%S %p"
                )
            )

        elif lower == "date":

            return (
                "📅 " +
                datetime.now().strftime(
                    "%d-%m-%Y"
                )
            )

        elif lower == "quote":

            return (
                "💡 " +
                self.get_quote()
            )

        elif lower == "help":

            return self.help_menu()

        elif lower == "bye":

            return (
                "👋 Goodbye! Have a productive day."
            )

        # ==================================
        # NOTES
        # ==================================

        elif lower.startswith(
            "add note "
        ):

            note = command[9:]

            if notes_manager:
                notes_manager.add_note(
                    note
                )

            return "📝 Note Added Successfully"

        elif lower == "show notes":

            if not notes_manager:
                return "Notes Manager Unavailable"

            notes = notes_manager.get_notes()

            if not notes:
                return "No Notes Found"

            result = "📝 NOTES\n\n"

            for i, note in enumerate(notes):

                result += (
                    f"{i+1}. {note}\n"
                )

            return result

        elif lower.startswith(
            "delete note "
        ):

            try:

                index = int(
                    lower.replace(
                        "delete note ",
                        ""
                    )
                ) - 1

                if notes_manager.delete_note(
                    index
                ):
                    return "🗑 Note Deleted"

                return "Invalid Note Number"

            except:

                return "Invalid Note Number"

        # ==================================
        # TASKS
        # ==================================

        elif lower.startswith(
            "add task "
        ):

            task = command[9:]

            if tasks_manager:
                tasks_manager.add_task(
                    task
                )

            return "✅ Task Added"

        elif lower == "show tasks":

            if not tasks_manager:
                return "Tasks Manager Unavailable"

            tasks = tasks_manager.get_tasks()

            if not tasks:
                return "No Tasks Found"

            result = "✅ TASKS\n\n"

            for i, task in enumerate(tasks):

                result += (
                    f"{i+1}. {task}\n"
                )

            return result

        elif lower.startswith(
            "complete task "
        ):

            try:

                index = int(
                    lower.replace(
                        "complete task ",
                        ""
                    )
                ) - 1

                if tasks_manager.complete_task(
                    index
                ):
                    return "✔ Task Completed"

                return "Invalid Task Number"

            except:

                return "Invalid Task Number"

        elif lower.startswith(
            "delete task "
        ):

            try:

                index = int(
                    lower.replace(
                        "delete task ",
                        ""
                    )
                ) - 1

                if tasks_manager.delete_task(
                    index
                ):
                    return "🗑 Task Deleted"

                return "Invalid Task Number"

            except:

                return "Invalid Task Number"

        # ==================================
        # GOALS
        # ==================================

        elif lower.startswith(
            "add goal "
        ):

            goal = command[9:]

            if goals_manager:
                goals_manager.add_goal(
                    goal
                )

            return "🎯 Goal Added"

        elif lower == "show goals":

            if not goals_manager:
                return "Goals Manager Unavailable"

            goals = goals_manager.get_goals()

            if not goals:
                return "No Goals Found"

            result = "🎯 GOALS\n\n"

            for i, goal in enumerate(goals):

                result += (
                    f"{i+1}. {goal}\n"
                )

            return result

        elif lower.startswith(
            "complete goal "
        ):

            try:

                index = int(
                    lower.replace(
                        "complete goal ",
                        ""
                    )
                ) - 1

                if goals_manager.complete_goal(
                    index
                ):
                    return "🏆 Goal Completed"

                return "Invalid Goal Number"

            except:

                return "Invalid Goal Number"

        elif lower.startswith(
            "delete goal "
        ):

            try:

                index = int(
                    lower.replace(
                        "delete goal ",
                        ""
                    )
                ) - 1

                if goals_manager.delete_goal(
                    index
                ):
                    return "🗑 Goal Deleted"

                return "Invalid Goal Number"

            except:

                return "Invalid Goal Number"

        # ==================================
        # CALCULATOR
        # ==================================

        elif lower.startswith(
            "calculate "
        ):

            expression = command[10:]

            return self.calculate(
                expression
            )

        # ==================================
        # STATS
        # ==================================

        elif lower == "stats":

            if stats_callback:
                return stats_callback()

            return "Statistics Unavailable"

        # ==================================
        # EXPORT REPORT
        # ==================================

        elif lower == "export report":

            if export_callback:
                return export_callback()

            return "Export Unavailable"

        # ==================================
        # UNKNOWN COMMAND
        # ==================================

        return (
            "❓ Unknown Command\n"
            "Type HELP to view commands."
        )