import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):

    length_criteria = len(password) >= 12
    lowercase_criteria = any(char.islower() for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        return "Strong", score, ["✅ Length is 12+ characters",
                                 "✅ Includes lowercase letters",
                                 "✅ Includes uppercase letters",
                                 "✅ Includes numbers",
                                 "✅ Includes special characters"]
    elif 3 <= score < 5:
        return "Medium", score, [("✅" if length_criteria else "❌") + " Length is 12+ characters",
                                 ("✅" if lowercase_criteria else "❌") + " Includes lowercase letters",
                                 ("✅" if uppercase_criteria else "❌") + " Includes uppercase letters",
                                 ("✅" if number_criteria else "❌") + " Includes numbers",
                                 ("✅" if special_char_criteria else "❌") + " Includes special characters"]
    else:
        return "Weak", score, [("✅" if length_criteria else "❌") + " Length is 12+ characters",
                               ("✅" if lowercase_criteria else "❌") + " Includes lowercase letters",
                               ("✅" if uppercase_criteria else "❌") + " Includes uppercase letters",
                               ("✅" if number_criteria else "❌") + " Includes numbers",
                               ("✅" if special_char_criteria else "❌") + " Includes special characters"]

def evaluate_password():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password!")
        return

    strength, score, feedback = check_password_strength(password)

    result_label.config(
        text=f"Password Strength: {strength} ({score}/5)",
        fg="lime" if strength == "Strong" else "gold" if strength == "Medium" else "red",
    )
    feedback_text.set("\n".join(feedback))

app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("450x400")
app.resizable(False, False)
app.configure(bg="#121212")  

font_primary = ("Helvetica Neue", 14)
font_secondary = ("Helvetica Neue", 12)
font_feedback = ("Helvetica Neue", 10)

tk.Label(
    app, text="Password Strength Checker", font=("Helvetica Neue", 18, "bold"), bg="#121212", fg="#ffffff"
).pack(pady=10)

tk.Label(
    app, text="Enter your password:", font=font_secondary, bg="#121212", fg="#ffffff"
).pack(pady=5)

password_entry = tk.Entry(
    app, show="*", width=30, font=font_primary, bg="#1e1e1e", fg="#ffffff", insertbackground="#ffffff", relief="flat"
)
password_entry.pack(pady=10)

check_button = tk.Button(
    app, text="Check Strength", command=evaluate_password, font=font_secondary, bg="#3a3a3a", fg="#ffffff", relief="flat"
)
check_button.pack(pady=15)

result_label = tk.Label(app, text="", font=("Helvetica Neue", 16, "bold"), bg="#121212", fg="#ffffff")
result_label.pack(pady=10)

feedback_text = tk.StringVar()
feedback_label = tk.Label(
    app, textvariable=feedback_text, font=font_feedback, bg="#121212", fg="#cfcfcf", justify="left"
)
feedback_label.pack(pady=10)

app.mainloop()
