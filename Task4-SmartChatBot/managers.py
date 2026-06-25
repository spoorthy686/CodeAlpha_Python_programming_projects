import os


# ==========================================
# BASE MANAGER
# ==========================================

class BaseManager:

    def __init__(self, file_path):

        self.file_path = file_path

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        if not os.path.exists(file_path):

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ):
                pass

    def read_all(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return [
                line.strip()
                for line in file.readlines()
                if line.strip()
            ]

    def write_all(self, data):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            for item in data:

                file.write(
                    item + "\n"
                )

    def append(self, text):

        with open(
            self.file_path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                text + "\n"
            )


# ==========================================
# NOTES MANAGER
# ==========================================

class NotesManager(BaseManager):

    def add_note(self, note):

        self.append(note)

    def get_notes(self):

        return self.read_all()

    def delete_note(self, index):

        notes = self.get_notes()

        if index < 0 or index >= len(notes):
            return False

        notes.pop(index)

        self.write_all(notes)

        return True

    def count(self):

        return len(self.get_notes())


# ==========================================
# TASKS MANAGER
# ==========================================

class TasksManager(BaseManager):

    def add_task(self, task):

        self.append(
            f"⭕ {task}"
        )

    def get_tasks(self):

        return self.read_all()

    def complete_task(self, index):

        tasks = self.get_tasks()

        if index < 0 or index >= len(tasks):
            return False

        task = tasks[index]

        if task.startswith("⭕"):

            task = task.replace(
                "⭕",
                "✅",
                1
            )

        tasks[index] = task

        self.write_all(tasks)

        return True

    def delete_task(self, index):

        tasks = self.get_tasks()

        if index < 0 or index >= len(tasks):
            return False

        tasks.pop(index)

        self.write_all(tasks)

        return True

    def pending_tasks(self):

        return len([
            task
            for task in self.get_tasks()
            if task.startswith("⭕")
        ])

    def completed_tasks(self):

        return len([
            task
            for task in self.get_tasks()
            if task.startswith("✅")
        ])

    def count(self):

        return len(self.get_tasks())


# ==========================================
# GOALS MANAGER
# ==========================================

class GoalsManager(BaseManager):

    def add_goal(self, goal):

        self.append(
            f"🎯 {goal}"
        )

    def get_goals(self):

        return self.read_all()

    def complete_goal(self, index):

        goals = self.get_goals()

        if index < 0 or index >= len(goals):
            return False

        goal = goals[index]

        if goal.startswith("🎯"):

            goal = goal.replace(
                "🎯",
                "🏆",
                1
            )

        goals[index] = goal

        self.write_all(goals)

        return True

    def delete_goal(self, index):

        goals = self.get_goals()

        if index < 0 or index >= len(goals):
            return False

        goals.pop(index)

        self.write_all(goals)

        return True

    def active_goals(self):

        return len([
            goal
            for goal in self.get_goals()
            if goal.startswith("🎯")
        ])

    def completed_goals(self):

        return len([
            goal
            for goal in self.get_goals()
            if goal.startswith("🏆")
        ])

    def count(self):

        return len(self.get_goals())


# ==========================================
# CHAT HISTORY MANAGER
# ==========================================

class ChatHistoryManager(BaseManager):

    def add_message(
        self,
        sender,
        message
    ):

        self.append(
            f"{sender}: {message}"
        )

    def get_history(self):

        return self.read_all()

    def clear_history(self):

        self.write_all([])

    def count(self):

        return len(
            self.get_history()
        )


# ==========================================
# FACTORY FUNCTION
# ==========================================

def create_managers():

    notes_manager = NotesManager(
        "data/notes.txt"
    )

    tasks_manager = TasksManager(
        "data/tasks.txt"
    )

    goals_manager = GoalsManager(
        "data/goals.txt"
    )

    history_manager = ChatHistoryManager(
        "data/chat_history.txt"
    )

    return (
        notes_manager,
        tasks_manager,
        goals_manager,
        history_manager
    )