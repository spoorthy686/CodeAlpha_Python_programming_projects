import os
import re
import shutil
import requests
import logging
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import hashlib

# -----------------------------
# WINDOW
# -----------------------------

root = Tk()
root.title("Smart Automation Hub")
root.geometry("1000x700")
root.configure(bg="#1E1E2E")

# -----------------------------
# LOGGING
# -----------------------------

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# -----------------------------
# REPORTS
# -----------------------------

os.makedirs("reports", exist_ok=True)

# -----------------------------
# FILE TYPES
# -----------------------------

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".java", ".html", ".css", ".js"]
}

# -----------------------------
# GUI FUNCTIONS
# -----------------------------

selected_folder = ""

def choose_folder():
    global selected_folder

    selected_folder = filedialog.askdirectory()

    folder_label.config(
        text=f"Selected: {selected_folder}"
    )
def fetch_quote():

    try:

        response = requests.get(
            "https://zenquotes.io/api/random",
            timeout=5
        )

        data = response.json()

        return data[0]["q"]

    except:

        return "Quote unavailable"
def get_file_hash(file_path):

    md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                md5.update(chunk)

        return md5.hexdigest()

    except Exception:
        return None

def extract_emails():

    emails = set()

    for file in os.listdir(selected_folder):

        if file.endswith(".txt"):

            path = os.path.join(
                selected_folder,
                file
            )

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                content = f.read()

            found = re.findall(
                r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
                content
            )

            emails.update(found)

    with open(
        "reports/extracted_emails.txt",
        "w"
    ) as f:

        for email in emails:
            f.write(email + "\n")

    return len(emails)

def organize_files():

    if not selected_folder:

        messagebox.showerror(
            "Error",
            "Select Folder First"
        )

        return

    destination = "OrganizedFiles"

    os.makedirs(destination, exist_ok=True)

    duplicate_folder = os.path.join(
        destination,
        "Duplicate_Files"
    )

    os.makedirs(
        duplicate_folder,
        exist_ok=True
    )

    stats = {}
    organized = 0
    duplicate_count = 0

    hashes = {}

    # Extract emails before moving files
    email_count = extract_emails()

    for file in os.listdir(selected_folder):

        path = os.path.join(
            selected_folder,
            file
        )

        if not os.path.isfile(path):
            continue

        # Check duplicate using hash
        file_hash = get_file_hash(path)

        if file_hash in hashes:

            shutil.move(
                path,
                os.path.join(
                    duplicate_folder,
                    file
                )
            )

            duplicate_count += 1

            logging.info(
                f"Duplicate moved: {file}"
            )

            continue

        hashes[file_hash] = file

        extension = os.path.splitext(
            file
        )[1].lower()

        moved = False

        for category, exts in FILE_TYPES.items():

            if extension in exts:

                category_folder = os.path.join(
                    destination,
                    category
                )

                os.makedirs(
                    category_folder,
                    exist_ok=True
                )

                shutil.move(
                    path,
                    os.path.join(
                        category_folder,
                        file
                    )
                )

                stats[category] = stats.get(
                    category,
                    0
                ) + 1

                organized += 1

                logging.info(
                    f"Moved {file} -> {category}"
                )

                moved = True
                break

        if not moved:

            other_folder = os.path.join(
                destination,
                "Others"
            )

            os.makedirs(
                other_folder,
                exist_ok=True
            )

            shutil.move(
                path,
                os.path.join(
                    other_folder,
                    file
                )
            )

            stats["Others"] = stats.get(
                "Others",
                0
            ) + 1

            organized += 1

    quote = fetch_quote()

    with open(
        "reports/report.txt",
        "w"
    ) as report:

        report.write(
            "SMART AUTOMATION HUB REPORT\n"
        )

        report.write(
            "=" * 40 + "\n\n"
        )

        report.write(
            f"Generated: {datetime.now()}\n\n"
        )

        report.write(
            f"Files Organized: {organized}\n"
        )

        report.write(
            f"Duplicate Files: {duplicate_count}\n"
        )

        report.write(
            f"Emails Extracted: {email_count}\n\n"
        )

        report.write(
            "Category Statistics\n"
        )

        report.write(
            "-" * 25 + "\n"
        )

        for category, count in stats.items():

            report.write(
                f"{category}: {count}\n"
            )

        report.write(
            "\nQuote Of The Day:\n"
        )

        report.write(
            quote
        )

    output.delete(
        1.0,
        END
    )

    output.insert(
        END,
        f"Files Organized: {organized}\n"
    )

    output.insert(
        END,
        f"Duplicate Files: {duplicate_count}\n"
    )

    output.insert(
        END,
        f"Emails Found: {email_count}\n\n"
    )

    output.insert(
        END,
        "Quote Of The Day:\n\n"
    )

    output.insert(
        END,
        quote
    )

    messagebox.showinfo(
        "Success",
        f"Automation Completed!\n\n"
        f"Files Organized: {organized}\n"
        f"Duplicates Found: {duplicate_count}"
    )
# -----------------------------
# -----------------------------
# TITLE
# -----------------------------

Label(
    root,
    text="SMART AUTOMATION HUB",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E2E",
    fg="#00E5FF"
).pack(pady=20)

# -----------------------------
# BUTTONS
# -----------------------------

Button(
    root,
    text="Select Folder",
    font=("Segoe UI", 14),
    bg="#00C853",
    fg="white",
    command=choose_folder
).pack(pady=10)

folder_label = Label(
    root,
    text="No Folder Selected",
    bg="#1E1E2E",
    fg="white",
    font=("Segoe UI", 11)
)

folder_label.pack()

Button(
    root,
    text="Run Automation",
    font=("Segoe UI", 14),
    bg="#2962FF",
    fg="white",
    command=organize_files
).pack(pady=15)

# -----------------------------
# OUTPUT BOX
# -----------------------------

output = ScrolledText(
    root,
    width=90,
    height=20,
    font=("Consolas", 12),
    bg="#2D2D44",
    fg="white"
)

output.pack(pady=20)

root.mainloop()