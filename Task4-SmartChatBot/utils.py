from datetime import datetime
import os


# ==========================================
# DATE & TIME UTILITIES
# ==========================================

def get_current_time():

    return datetime.now().strftime(
        "%I:%M:%S %p"
    )


def get_current_date():

    return datetime.now().strftime(
        "%d-%m-%Y"
    )


# ==========================================
# SESSION TIMER
# ==========================================

class SessionTimer:

    def __init__(self):

        self.start_time = datetime.now()

    def get_minutes(self):

        seconds = (
            datetime.now() -
            self.start_time
        ).total_seconds()

        return int(seconds // 60)

    def get_seconds(self):

        seconds = (
            datetime.now() -
            self.start_time
        ).total_seconds()

        return int(seconds)

    def get_formatted_time(self):

        total = self.get_seconds()

        hours = total // 3600

        minutes = (
            total % 3600
        ) // 60

        seconds = total % 60

        return (
            f"{hours:02d}:"
            f"{minutes:02d}:"
            f"{seconds:02d}"
        )


# ==========================================
# PRODUCTIVITY SCORE
# ==========================================

def productivity_score(
    tasks_manager,
    goals_manager
):

    completed_tasks = (
        tasks_manager.completed_tasks()
    )

    total_tasks = (
        tasks_manager.count()
    )

    completed_goals = (
        goals_manager.completed_goals()
    )

    total_goals = (
        goals_manager.count()
    )

    task_score = 0
    goal_score = 0

    if total_tasks > 0:

        task_score = (
            completed_tasks /
            total_tasks
        ) * 50

    if total_goals > 0:

        goal_score = (
            completed_goals /
            total_goals
        ) * 50

    return round(
        task_score +
        goal_score,
        2
    )


# ==========================================
# STATISTICS ENGINE
# ==========================================

def generate_stats(
    notes_manager,
    tasks_manager,
    goals_manager,
    history_manager
):

    stats = {

        "notes":
        notes_manager.count(),

        "tasks":
        tasks_manager.count(),

        "completed_tasks":
        tasks_manager.completed_tasks(),

        "pending_tasks":
        tasks_manager.pending_tasks(),

        "goals":
        goals_manager.count(),

        "completed_goals":
        goals_manager.completed_goals(),

        "active_goals":
        goals_manager.active_goals(),

        "messages":
        history_manager.count()
    }

    return stats


def stats_text(
    notes_manager,
    tasks_manager,
    goals_manager,
    history_manager
):

    stats = generate_stats(
        notes_manager,
        tasks_manager,
        goals_manager,
        history_manager
    )

    score = productivity_score(
        tasks_manager,
        goals_manager
    )

    return f"""
📊 SMART ASSISTANT STATISTICS

📝 Notes:
{stats['notes']}

✅ Tasks:
{stats['tasks']}

✔ Completed Tasks:
{stats['completed_tasks']}

⭕ Pending Tasks:
{stats['pending_tasks']}

🎯 Goals:
{stats['goals']}

🏆 Completed Goals:
{stats['completed_goals']}

🚀 Active Goals:
{stats['active_goals']}

💬 Messages:
{stats['messages']}

⭐ Productivity Score:
{score}%
"""


# ==========================================
# REPORT EXPORTER
# ==========================================

def export_report(
    notes_manager,
    tasks_manager,
    goals_manager,
    history_manager
):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    report_file = (
        "reports/"
        "assistant_report.txt"
    )

    score = productivity_score(
        tasks_manager,
        goals_manager
    )

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "SMART ASSISTANT PRO REPORT\n"
        )

        report.write(
            "=" * 50 + "\n\n"
        )

        report.write(
            f"Generated: "
            f"{datetime.now()}\n\n"
        )

        report.write(
            "NOTES\n"
        )

        report.write(
            "-" * 30 + "\n"
        )

        for note in notes_manager.get_notes():

            report.write(
                note + "\n"
            )

        report.write(
            "\nTASKS\n"
        )

        report.write(
            "-" * 30 + "\n"
        )

        for task in tasks_manager.get_tasks():

            report.write(
                task + "\n"
            )

        report.write(
            "\nGOALS\n"
        )

        report.write(
            "-" * 30 + "\n"
        )

        for goal in goals_manager.get_goals():

            report.write(
                goal + "\n"
            )

        report.write(
            "\nCHAT HISTORY\n"
        )

        report.write(
            "-" * 30 + "\n"
        )

        for msg in history_manager.get_history():

            report.write(
                msg + "\n"
            )

        report.write(
            "\nPRODUCTIVITY SCORE\n"
        )

        report.write(
            "-" * 30 + "\n"
        )

        report.write(
            f"{score}%"
        )

    return (
        "Report exported successfully:\n"
        + report_file
    )


# ==========================================
# QUOTES
# ==========================================

def motivational_quote():

    quotes = [

        "Success is built one step at a time.",

        "Consistency beats motivation.",

        "Small progress is still progress.",

        "Focus on improvement, not perfection.",

        "Discipline creates freedom.",

        "Your future is created by what you do today."
    ]

    import random

    return random.choice(
        quotes
    )