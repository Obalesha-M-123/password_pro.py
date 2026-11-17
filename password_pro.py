import tkinter as tk
from tkinter import ttk

def check_password():
    password = entry.get()
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add a number")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        suggestions.append("Add a special character")

    progress["value"] = score * 20

    if score <= 2:
        strength.config(text="WEAK", fg="red")
        progress.configure(style="Red.Horizontal.TProgressbar")
    elif score <= 4:
        strength.config(text="MEDIUM", fg="orange")
        progress.configure(style="Yellow.Horizontal.TProgressbar")
    else:
        strength.config(text="STRONG", fg="lime")
        progress.configure(style="Green.Horizontal.TProgressbar")

    score_label.config(text=f"Password Score: {score}/5")

    if suggestions:
        result.config(
            text="Suggestions:\n" + "\n".join(
                "- " + item for item in suggestions
            ),
            fg="orange"
        )
    else:
        result.config(
            text="Excellent! Strong password!",
            fg="lime"
        )


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        show_btn.config(text="Hide")
    else:
        entry.config(show="*")
        show_btn.config(text="Show")


def reset():
    entry.delete(0, tk.END)
    progress["value"] = 0
    strength.config(text="Not Checked", fg="white")
    score_label.config(text="Password Score: 0/5")
    result.config(text="")
    entry.focus()


root = tk.Tk()
root.title("Password Analyzer PRO")
root.geometry("550x620")
root.configure(bg="#172554")
root.resizable(False, False)

title = tk.Label(
    root,
    text="PASSWORD ANALYZER PRO",
    font=("Arial", 22, "bold"),
    bg="#172554",
    fg="cyan"
)
title.pack(pady=25)

tk.Label(
    root,
    text="Check Your Password Security",
    font=("Arial", 12),
    bg="#172554",
    fg="white"
).pack(pady=5)

entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    show="*",
    bg="#ffffff"
)
entry.pack(pady=20)

show_btn = tk.Button(
    root,
    text="Show",
    command=toggle_password,
    bg="#2563eb",
    fg="white"
)
show_btn.pack()

tk.Button(
    root,
    text="CHECK PASSWORD",
    command=check_password,
    font=("Arial", 12, "bold"),
    bg="#0891b2",
    fg="white",
    width=22
).pack(pady=20)

strength = tk.Label(
    root,
    text="Not Checked",
    font=("Arial", 18, "bold"),
    bg="#172554",
    fg="white"
)
strength.pack(pady=10)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Red.Horizontal.TProgressbar",
    troughcolor="white",
    background="red"
)
style.configure(
    "Yellow.Horizontal.TProgressbar",
    troughcolor="white",
    background="orange"
)
style.configure(
    "Green.Horizontal.TProgressbar",
    troughcolor="white",
    background="lime"
)

progress = ttk.Progressbar(
    root,
    length=350,
    maximum=100,
    mode="determinate",
    style="Red.Horizontal.TProgressbar"
)
progress.pack(pady=10)

score_label = tk.Label(
    root,
    text="Password Score: 0/5",
    font=("Arial", 13, "bold"),
    bg="#172554",
    fg="white"
)
score_label.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#172554",
    fg="white",
    justify="left"
)
result.pack(pady=15)

tk.Button(
    root,
    text="RESET",
    command=reset,
    font=("Arial", 11, "bold"),
    bg="#dc2626",
    fg="white",
    width=15
).pack(pady=15)

root.mainloop()