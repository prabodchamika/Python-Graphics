import tkinter as tk
from tkinter import messagebox

def calculate_gpa():
    try:
        grades = [float(entry[0].get()) for entry in course_entries]
        credits = [float(entry[1].get()) for entry in course_entries]
        
        total_points = sum(grade * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
        
        if total_credits == 0:
            raise ValueError("Total credits cannot be zero.")
        
        gpa = total_points / total_credits
        result_label.config(text=f"GPA: {gpa:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def add_course():
    row = len(course_entries) + 1
    
    grade_entry = tk.Entry(frame, bg="#2c2c2e", fg="#f2f2f7", insertbackground="#f2f2f7")
    grade_entry.grid(row=row, column=0, padx=10, pady=5)

    credit_entry = tk.Entry(frame, bg="#2c2c2e", fg="#f2f2f7", insertbackground="#f2f2f7")
    credit_entry.grid(row=row, column=1, padx=10, pady=5)

    remove_button = tk.Button(frame, text="Remove", bg="#ff3b30", fg="#f2f2f7", command=lambda: remove_course(row))
    remove_button.grid(row=row, column=2, padx=10, pady=5)

    course_entries.append((grade_entry, credit_entry, remove_button))

def remove_course(row):
    for widget in frame.grid_slaves():
        if widget.grid_info()["row"] == row:
            widget.destroy()
    course_entries.pop(row - 1)

    for i, entry in enumerate(course_entries):
        entry[0].grid(row=i + 1, column=0)
        entry[1].grid(row=i + 1, column=1)
        entry[2].grid(row=i + 1, column=2)

root = tk.Tk()
root.title("GPA Calculator")
root.geometry("450x450")
root.configure(bg="#1c1c1e")

title_label = tk.Label(root, text="GPA Calculator", bg="#1c1c1e", fg="#f2f2f7", font=("Helvetica", 18))
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#1c1c1e")
frame.pack(pady=10)

header_labels = ["Grade", "Credits", "Actions"]
for col, text in enumerate(header_labels):
    tk.Label(frame, text=text, bg="#1c1c1e", fg="#f2f2f7").grid(row=0, column=col, padx=10, pady=5)

course_entries = []
add_course()

add_course_button = tk.Button(root, text="Add Course", bg="#2c2c2e", fg="#f2f2f7", command=add_course)
add_course_button.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate GPA", bg="#2c2c2e", fg="#f2f2f7", command=calculate_gpa)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="GPA: --", bg="#1c1c1e", fg="#f2f2f7", font=("Helvetica", 16))
result_label.pack(pady=10)

root.mainloop()
