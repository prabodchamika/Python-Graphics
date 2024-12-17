import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    char_pool = lowercase
    if use_uppercase: char_pool += uppercase
    if use_digits: char_pool += digits
    if use_special_chars: char_pool += special_chars

    password = ''.join(random.choice(char_pool) for _ in range(length))
    result_label.config(text=f"Generated Password:\n{password}")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x450")
root.configure(bg="#1c1c1e")

title_label = tk.Label(root, text="Random Password Generator", bg="#1c1c1e", fg="#f2f2f7", font=("Helvetica", 18))
title_label.pack(pady=10)

length_label = tk.Label(root, text="Password Length", bg="#1c1c1e", fg="#f2f2f7", font=("Helvetica", 12))
length_label.pack(pady=5)
length_entry = tk.Entry(root, bg="#2c2c2e", fg="#f2f2f7", insertbackground="#f2f2f7", font=("Helvetica", 12))
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root, bg="#1c1c1e")
options_frame.pack(pady=10)
tk.Checkbutton(options_frame, text="Include Uppercase", bg="#1c1c1e", fg="#f2f2f7", variable=uppercase_var,
                selectcolor="#3e3e3e", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Include Digits", bg="#1c1c1e", fg="#f2f2f7", variable=digits_var,
                selectcolor="#3e3e3e", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Include Special Chars", bg="#1c1c1e", fg="#f2f2f7", variable=special_chars_var, 
               selectcolor="#3e3e3e", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w")

generate_button = tk.Button(root, text="Generate Password", bg="#2c2c2e", fg="#f2f2f7",
                             font=("Helvetica", 12), command=generate_password)
generate_button.pack(pady=15)

result_label = tk.Label(root, text="Generated Password:\n--", bg="#1c1c1e", fg="#f2f2f7",
                         font=("Helvetica", 14), justify="center")
result_label.pack(pady=10)

root.mainloop()
