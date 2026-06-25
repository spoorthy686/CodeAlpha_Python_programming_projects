import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from chatbot import ChatBotEngine
from managers import create_managers
from utils import (
    SessionTimer,
    stats_text,
    export_report,
    get_current_time,
    motivational_quote
)

# ==========================================
# APP SETTINGS
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==========================================
# WINDOW
# ==========================================

root = ctk.CTk()

root.title("Smart Assistant Pro")
root.geometry("1600x900")
root.minsize(1200, 700)

# ==========================================
# DATA MANAGERS
# ==========================================

(
    notes_manager,
    tasks_manager,
    goals_manager,
    history_manager
) = create_managers()

# ==========================================
# CHATBOT
# ==========================================

bot = ChatBotEngine()

# ==========================================
# SESSION TIMER
# ==========================================

timer = SessionTimer()

# ==========================================
# GLOBALS
# ==========================================

message_count = 0
current_theme = "dark"

# ==========================================
# MAIN CONTAINER
# ==========================================

container = ctk.CTkFrame(
    root,
    fg_color="transparent"
)

container.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# ==========================================
# SIDEBAR
# ==========================================

sidebar = ctk.CTkScrollableFrame(
    container,
    width=280,
    corner_radius=15
)

sidebar.pack(
    side="left",
    fill="y",
    padx=(0, 10)
)

# ==========================================
# LOGO
# ==========================================

logo = ctk.CTkLabel(
    sidebar,
    text="🤖\nSMART ASSISTANT PRO",
    font=("Segoe UI", 24, "bold")
)

logo.pack(
    pady=20
)

# ==========================================
# NAVIGATION TITLE
# ==========================================

nav_title = ctk.CTkLabel(
    sidebar,
    text="Navigation",
    font=("Segoe UI", 18, "bold")
)

nav_title.pack(
    pady=(10, 10)
)

# ==========================================
# NAV BUTTONS
# ==========================================

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="🏠 Dashboard"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

assistant_btn = ctk.CTkButton(
    sidebar,
    text="🤖 Assistant"
)

assistant_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

notes_btn = ctk.CTkButton(
    sidebar,
    text="📝 Notes"
)

notes_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

tasks_btn = ctk.CTkButton(
    sidebar,
    text="✅ Tasks"
)

tasks_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

goals_btn = ctk.CTkButton(
    sidebar,
    text="🎯 Goals"
)

goals_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

reports_btn = ctk.CTkButton(
    sidebar,
    text="📁 Reports"
)

reports_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

settings_btn = ctk.CTkButton(
    sidebar,
    text="⚙ Settings"
)

settings_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

# ==========================================
# DASHBOARD TITLE
# ==========================================

dashboard_title = ctk.CTkLabel(
    sidebar,
    text="📊 Dashboard",
    font=("Segoe UI", 18, "bold")
)

dashboard_title.pack(
    pady=(20, 10)
)

# ==========================================
# DASHBOARD CARD FUNCTION
# ==========================================

def create_card(title, value):

    frame = ctk.CTkFrame(
        sidebar,
        height=90,
        corner_radius=15
    )

    frame.pack(
        fill="x",
        padx=10,
        pady=8
    )

    label_title = ctk.CTkLabel(
        frame,
        text=title,
        font=("Segoe UI", 13, "bold")
    )

    label_title.pack(
        pady=(10, 0)
    )

    label_value = ctk.CTkLabel(
        frame,
        text=value,
        font=("Segoe UI", 22, "bold")
    )

    label_value.pack(
        pady=(5, 10)
    )

    return label_value

# ==========================================
# DASHBOARD CARDS
# ==========================================

messages_card = create_card(
    "💬 Messages",
    "0"
)

notes_card = create_card(
    "📝 Notes",
    "0"
)

tasks_card = create_card(
    "✅ Tasks",
    "0"
)

goals_card = create_card(
    "🎯 Goals",
    "0"
)

session_card = create_card(
    "⏱ Session",
    "00:00:00"
)

time_card = create_card(
    "⌚ Time",
    "--:--"
)

# ==========================================
# MAIN AREA
# ==========================================

main_frame = ctk.CTkFrame(
    container,
    corner_radius=15
)

main_frame.pack(
    side="right",
    fill="both",
    expand=True
)

# ==========================================
# HEADER
# ==========================================

header = ctk.CTkFrame(
    main_frame,
    height=70
)

header.pack(
    fill="x",
    padx=10,
    pady=10
)

title_label = ctk.CTkLabel(
    header,
    text="💬 Smart Assistant Pro",
    font=("Segoe UI", 26, "bold")
)

title_label.pack(
    side="left",
    padx=20
)

# ==========================================
# THEME TOGGLE
# ==========================================
def toggle_theme():

    global current_theme

    try:

        if ctk.get_appearance_mode() == "Dark":

            ctk.set_appearance_mode("Light")

            current_theme = "light"

            theme_btn.configure(
                text="🌙 Dark Mode"
            )

        else:

            ctk.set_appearance_mode("Dark")

            current_theme = "dark"

            theme_btn.configure(
                text="☀ Light Mode"
            )

        root.update()

    except Exception as e:

        print("Theme Error:", e)
        theme_btn = ctk.CTkButton(
        header,
        text="🌙 Dark",
        width=120,
        command=toggle_theme
)

        theme_btn.pack(
        side="right",
        padx=20
)
# ==========================================
# CHAT AREA
# ==========================================

chat_container = ctk.CTkFrame(
    main_frame,
    corner_radius=15
)

chat_container.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)

# ==========================================
# CHAT SCROLLABLE AREA
# ==========================================

chat_area = ctk.CTkScrollableFrame(
    chat_container,
    corner_radius=10
)

chat_area.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)
root.after(
    500,
    #scroll_to_bottom
)
# ==========================================
# AUTO SCROLL
# ==========================================
def scroll_to_bottom():

    try:

        root.update()

        canvas = chat_area._parent_canvas

        canvas.update_idletasks()

        canvas.yview_moveto(1.0)

    except Exception as e:

        print("Scroll Error:", e)
    

# ==========================================
# BOT BUBBLE
# ==========================================
def add_bot_message(message):

    outer = ctk.CTkFrame(
        chat_area,
        fg_color="transparent"
    )

    outer.pack(
        fill="x",
        pady=6,
        padx=15
    )

    bubble = ctk.CTkFrame(
        outer,
        corner_radius=20,
        fg_color=("#E5E7EB", "#2B2D42")
    )

    bubble.pack(anchor="w")

    msg = ctk.CTkLabel(
        bubble,
        text=message,
        wraplength=850,
        justify="left",
        font=("Segoe UI", 14)
    )

    msg.pack(
        padx=15,
        pady=12
    )

    root.after(
    200,
    scroll_to_bottom
)
# ==========================================
# USER BUBBLE
# ==========================================

def add_user_message(message):

    outer = ctk.CTkFrame(
        chat_area,
        fg_color="transparent"
    )

    outer.pack(
        fill="x",
        pady=6,
        padx=15
    )

    bubble = ctk.CTkFrame(
        outer,
        corner_radius=20,
        fg_color="#0B93F6"
    )

    bubble.pack(anchor="e")

    msg = ctk.CTkLabel(
        bubble,
        text=message,
        wraplength=850,
        justify="left",
        text_color="white",
        font=("Segoe UI", 14)
    )

    msg.pack(
        padx=15,
        pady=12
    )

    root.after(
    200,
    scroll_to_bottom
)

# ==========================================
# TYPING LABEL
# ==========================================

typing_label = ctk.CTkLabel(
    chat_container,
    text="",
    font=("Segoe UI", 12, "italic")
)

typing_label.pack(
    anchor="w",
    padx=20,
    pady=(0, 5)
)

def show_typing():

    typing_label.configure(
        text="🤖 Assistant is typing..."
    )

def hide_typing():

    typing_label.configure(
        text=""
    )

# ==========================================
# WELCOME MESSAGE
# ==========================================


# ==========================================
# INPUT AREA
# ==========================================

input_frame = ctk.CTkFrame(
    main_frame,
    corner_radius=15
)

input_frame.pack(
    fill="x",
    padx=10,
    pady=(0, 10)
)

user_entry = ctk.CTkEntry(
    input_frame,
    height=45,
    font=("Segoe UI", 14),
    placeholder_text="Type your message..."
)

user_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=10,
    pady=10
)

send_button = ctk.CTkButton(
    input_frame,
    text="SEND",
    width=140
)

send_button.pack(
    side="right",
    padx=10
)

# ==========================================
# STATUS BAR
# ==========================================

status_bar = ctk.CTkLabel(
    main_frame,
    text="Ready",
    anchor="w",
    height=28
)

status_bar.pack(
    fill="x",
    padx=10,
    pady=(0, 10)
)
# ==========================================
# SAVE CHAT HISTORY
# ==========================================

def save_chat(user_msg, bot_msg):

    history_manager.add_message(
        "USER",
        user_msg
    )

    history_manager.add_message(
        "BOT",
        bot_msg
    )

# ==========================================
# DASHBOARD UPDATE
# ==========================================

def update_dashboard():

    messages_card.configure(
        text=str(
            history_manager.count()
        )
    )

    notes_card.configure(
        text=str(
            notes_manager.count()
        )
    )

    tasks_card.configure(
        text=str(
            tasks_manager.count()
        )
    )

    goals_card.configure(
        text=str(
            goals_manager.count()
        )
    )

    session_card.configure(
        text=timer.get_formatted_time()
    )

    time_card.configure(
        text=get_current_time()
    )

# ==========================================
# STATISTICS CALLBACK
# ==========================================

def statistics_callback():

    return stats_text(
        notes_manager,
        tasks_manager,
        goals_manager,
        history_manager
    )

# ==========================================
# EXPORT CALLBACK
# ==========================================

def export_callback():

    return export_report(
        notes_manager,
        tasks_manager,
        goals_manager,
        history_manager
    )

# ==========================================
# LOAD OLD CHAT
# ==========================================

def load_history():

    history = (
        history_manager
        .get_history()
    )

    if not history:
        return

    for line in history:

        if line.startswith(
            "USER:"
        ):

            add_user_message(
                line.replace(
                    "USER:",
                    ""
                ).strip()
            )

        elif line.startswith(
            "BOT:"
        ):

            add_bot_message(
                line.replace(
                    "BOT:",
                    ""
                ).strip()
            )

# ==========================================
# TYPING EFFECT
# ==========================================

def simulate_typing(
    user_text
):

    show_typing()

    root.after(
        500,
        lambda:
        generate_response(
            user_text
        )
    )

# ==========================================
# GENERATE RESPONSE
# ==========================================

def generate_response(
    user_text
):

    hide_typing()

    bot_reply = bot.get_response(

        user_text,

        notes_manager=
        notes_manager,

        tasks_manager=
        tasks_manager,

        goals_manager=
        goals_manager,

        stats_callback=
        statistics_callback,

        export_callback=
        export_callback
    )

    add_bot_message(
        bot_reply
    )
    root.after(
    150,
    scroll_to_bottom
    )

    save_chat(
        user_text,
        bot_reply
    )

    update_dashboard()

# ==========================================
# SEND MESSAGE
# ==========================================

def send_message():

    global message_count

    user_text = (
        user_entry.get()
        .strip()
    )

    if not user_text:
        return

    add_user_message(
        user_text
    )

    user_entry.delete(
        0,
        "end"
    )

    message_count += 1

    simulate_typing(
        user_text
    )

# ==========================================
# BUTTON COMMAND
# ==========================================

send_button.configure(
    command=send_message
)

# ==========================================
# ENTER KEY SUPPORT
# ==========================================

user_entry.bind(
    "<Return>",
    lambda e:
    send_message()
)

# ==========================================
# QUICK SIDEBAR ACTIONS
# ==========================================

def show_help():

    add_bot_message(
        bot.help_menu()
    )

def show_notes():

    notes = notes_manager.get_notes()

    if not notes:

        add_bot_message(
            "No notes available."
        )

        return

    text = "\n".join([
        f"{i+1}. {n}"
        for i, n in enumerate(notes)
    ])

    add_bot_message(
        "📝 NOTES\n\n" + text
    )

def show_tasks():

    tasks = tasks_manager.get_tasks()

    if not tasks:

        add_bot_message(
            "No tasks available."
        )

        return

    text = "\n".join([
        f"{i+1}. {t}"
        for i, t in enumerate(tasks)
    ])

    add_bot_message(
        "✅ TASKS\n\n" + text
    )

def show_goals():

    goals = goals_manager.get_goals()

    if not goals:

        add_bot_message(
            "No goals available."
        )

        return

    text = "\n".join([
        f"{i+1}. {g}"
        for i, g in enumerate(goals)
    ])

    add_bot_message(
        "🎯 GOALS\n\n" + text
    )

# ==========================================
# CONNECT SIDEBAR BUTTONS
# ==========================================

assistant_btn.configure(
    command=show_help
)
notes_btn.configure(
    command=lambda:
    messagebox.showinfo(
        "Notes",
        "\n".join(notes_manager.get_notes())
        if notes_manager.get_notes()
        else "No Notes Found"
    )
)
tasks_btn.configure(
    command=lambda:
    messagebox.showinfo(
        "Tasks",
        "\n".join(tasks_manager.get_tasks())
        if tasks_manager.get_tasks()
        else "No Tasks Found"
    )
)
goals_btn.configure(
    command=lambda:
    messagebox.showinfo(
        "Goals",
        "\n".join(goals_manager.get_goals())
        if goals_manager.get_goals()
        else "No Goals Found"
    )
)
reports_btn.configure(
    command=lambda:
    add_bot_message(
        export_callback()
    )
)

# ==========================================
# AUTO REFRESH DASHBOARD
# ==========================================

def refresh_dashboard():

    update_dashboard()

    root.after(
        1000,
        refresh_dashboard
    )

refresh_dashboard()

# ==========================================
# LOAD PREVIOUS CHAT
# ==========================================

#load_history()
# ==========================================
# CLEAR CHAT
# ==========================================

def clear_chat():

    for widget in chat_area.winfo_children():

        widget.destroy()

    add_bot_message(
        "🧹 Chat cleared successfully."
    )

# ==========================================
# EXIT APPLICATION
# ==========================================

def exit_app():

    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit Smart Assistant Pro?"
    )

    if answer:

        root.destroy()

# ==========================================
# DASHBOARD SHORTCUTS
# ==========================================

def show_dashboard():

    stats = statistics_callback()

    add_bot_message(
        stats
    )

def show_quote():

    add_bot_message(
        "💡 " +
        motivational_quote()
    )

# ==========================================
# SETTINGS WINDOW
# ==========================================
def open_settings():

    settings_window = ctk.CTkToplevel(root)

    settings_window.title("Settings")
    settings_window.geometry("400x300")

    settings_window.transient(root)
    #settings_window.grab_set()

    title = ctk.CTkLabel(
        settings_window,
        text="⚙ Settings",
        font=("Segoe UI", 24, "bold")
    )
    title.pack(pady=20)

    theme_button = ctk.CTkButton(
        settings_window,
        text="Toggle Theme",
        command=toggle_theme
    )
    theme_button.pack(pady=10)

    clear_button = ctk.CTkButton(
        settings_window,
        text="Clear Chat",
        command=clear_chat
    )
    clear_button.pack(pady=10)

    export_button = ctk.CTkButton(
        settings_window,
        text="Export Report",
        command=lambda: add_bot_message(export_callback())
    )
    export_button.pack(pady=10)

# ==========================================
# CONNECT BUTTONS
# ==========================================

dashboard_btn.configure(
    command=show_dashboard
)

settings_btn.configure(
    command=open_settings
)

# ==========================================
# LIVE STATUS BAR
# ==========================================

def update_status_bar():

    current_time = datetime.now().strftime(
        "%I:%M:%S %p"
    )

    status_bar.configure(
        text=
        f"Smart Assistant Pro | "
        f"{current_time} | "
        f"Theme: {current_theme.upper()}"
    )

    root.after(
        1000,
        update_status_bar
    )

update_status_bar()

# ==========================================
# WINDOW CLOSE EVENT
# ==========================================

root.protocol(
    "WM_DELETE_WINDOW",
    exit_app
)

# ==========================================
# FINAL DASHBOARD UPDATE
# ==========================================

update_dashboard()
add_bot_message(
    "Hello! I'm Smart Assistant Pro. Type HELP to see available commands."
)
# ==========================================
# MAIN LOOP
# ==========================================

root.mainloop()
